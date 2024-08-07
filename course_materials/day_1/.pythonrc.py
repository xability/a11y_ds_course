"""Written by JooYoung Seo (jseo1005@illinois.edu)
The following works on Windows, Mac, and Linux universally.
Also works on both standard Python and IPython."""

import sys

# Store the original excepthook
original_excepthook = sys.excepthook


# Play beep for errors
def play_beep():
    try:
        import platform

        system = platform.system().lower()

        if system == "windows":
            import winsound

            winsound.Beep(1000, 250)  # 1000 Hz for 250 ms
        elif system == "darwin":  # macOS
            import os

            os.system("afplay /System/Library/Sounds/Ping.aiff")
        else:  # Linux and other Unix-like systems
            import os

            os.system("beep")
    except Exception:
        # If beep fails, we don't want to mask the original error
        pass


def custom_excepthook(exc_type, exc_value, exc_traceback):
    # Play the beep
    play_beep()

    # Import traceback here to avoid global import
    import traceback

    # Print the traceback as usual
    traceback.print_exception(exc_type, exc_value, exc_traceback)


# Store IPython's custom exception handler
ipython_custom_exc_handler = None


def initialize_error_beep():
    global ipython_custom_exc_handler

    # Set the custom exception hook for standard Python
    sys.excepthook = custom_excepthook

    # Check if we're in IPython
    try:
        __IPYTHON__
    except NameError:
        # We are not in IPython, we're done
        print(
            "Error beep system initialized for standard Python.\nUse `beep_off()` to turn off beep on errors."
        )
    else:
        # We are in IPython, so we need to set up custom exception handling
        try:
            from IPython.core.getipython import get_ipython
        except ImportError:
            print(
                "IPython is not available. Error beep might not work in IPython environment."
            )
            return

        ip = get_ipython()

        def custom_exc_handler(shell, etype, evalue, tb, tb_offset=None):
            # Play the beep
            play_beep()

            # Call IPython's default exception handler
            shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)

        # Store IPython's custom exception handler
        ipython_custom_exc_handler = custom_exc_handler

        # Set the custom exception handler for IPython
        ip.set_custom_exc((Exception,), custom_exc_handler)
        print("Error beep system initialized for IPython.")


# Make pandas DataFrame print more accessible
def custom_display_html(self):
    from great_tables import GT

    gt = GT(self)
    gt.show()
    return ""


def custom_display_str(self):
    from great_tables import GT

    gt = GT(self)
    gt.show()
    return ""


def set_custom_display():
    from pandas import DataFrame

    DataFrame._original_repr = DataFrame.__repr__
    DataFrame._repr_html_ = custom_display_html
    DataFrame.__repr__ = custom_display_str
    print(
        "HTML printing for pandas DataFrame is on.\nUse `table_off()` if you would like to go back to the default pandas print mode."
    )


# Added by Ken Perry
cdir = lambda x: [item for item in dir(x) if not item.startswith("_")]


# New function to turn off beeping
def beep_off():
    global ipython_custom_exc_handler

    # Turn off beeping for standard Python
    sys.excepthook = original_excepthook

    # Turn off beeping for IPython
    try:
        __IPYTHON__
        from IPython.core.getipython import get_ipython

        ip = get_ipython()
        ip.set_custom_exc((), None)
    except NameError:
        pass

    print("Error beep system turned off.")


# New function to restore original DataFrame printing behavior
def table_off():
    from pandas import DataFrame
    from pandas.io.formats import format as fmt

    # Restore original _repr_html_ method
    if hasattr(DataFrame, "_repr_html_"):
        del DataFrame._repr_html_

    # Restore original __repr__ method
    if hasattr(DataFrame, "_original_repr"):
        DataFrame.__repr__ = DataFrame._original_repr
    else:
        # If original __repr__ is not stored, use a default implementation
        def default_repr(self):
            return fmt.DataFrameFormatter(self).to_string()

        DataFrame.__repr__ = default_repr

    print("Original DataFrame printing behavior restored.")


# Call the initialization functions
initialize_error_beep()
set_custom_display()
