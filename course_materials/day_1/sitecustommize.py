import os
import site

# Determine the site-packages directory
try:
    site_packages = site.getsitepackages()[0]
except AttributeError:
    from distutils.sysconfig import get_python_lib

    site_packages = get_python_lib()

# Path to sitecustomize.py
sitecustomize_path = os.path.join(site_packages, "sitecustomize.py")

# Code to append (as a unique identifier)
code_identifier = (
    "# Added by Python script to load PYTHONSTARTUP without polluting namespace"
)

# Full code to append
code_to_append = f"""
{code_identifier}
def _run_startup():
    import os
    startup_file = os.environ.get('PYTHONSTARTUP')
    if startup_file and os.path.isfile(startup_file):
        with open(startup_file, 'r') as f:
            code = f.read()
        exec(code, globals())
    del os, startup_file, code  # Clean up local variables
_run_startup()
del _run_startup
"""


# Function to check if the code is already present
def is_code_already_present(file_path, identifier):
    if not os.path.exists(file_path):
        return False
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return identifier in content


# Check if the code is already present
if is_code_already_present(sitecustomize_path, code_identifier):
    print(
        f"The code to load PYTHONSTARTUP is already present in {sitecustomize_path}. No changes made."
    )
else:
    # Append the code
    with open(sitecustomize_path, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(code_to_append)
    print(f'Successfully updated sitecustomize.py at "{sitecustomize_path}"')
