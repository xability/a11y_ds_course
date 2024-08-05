"""Written by JooYoung Seo (jseo1005@illinois.edu)
The following works on Windows, Mac, and Linux universally.
Also works on both standard Python and IPython."""


# Play beep for errors
def play_beep():
    try:
        import platform

        system = platform.system().lower()

        if system == "windows":
            import winsound

            winsound.Beep(1000,250)  # 1000 Hz for 500 ms
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


def initialize_error_beep():
    # Import sys here to avoid global import
    import sys

    # Set the custom exception hook for standard Python
    sys.excepthook = custom_excepthook

    # Check if we're in IPython
    try:
        __IPYTHON__
    except NameError:
        # We are not in IPython, we're done
        print("Error beep system initialized for standard Python.")
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

        # Set the custom exception handler for IPython
        ip.set_custom_exc((Exception,), custom_exc_handler)
        print("Error beep system initialized for IPython.")


# Call the initialization function
initialize_error_beep()


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

    DataFrame._repr_html_ = custom_display_html
    DataFrame.__repr__ = custom_display_str


set_custom_display()

#Added by Ken Perry
cdir =lambda x : [item for item in dir(x) if not item.startswith("_")]
