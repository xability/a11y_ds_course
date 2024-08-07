@echo off
REM Step 1: Create IPython profile if not existing
ipython profile create

REM Get the IPython profile directory
for /f "tokens=*" %%i in ('ipython locate profile') do set IPYTHON_PROFILE_PATH=%%i

REM Step 2: Copy .pythonrc.py file to the startup folder under the IPython profile
set STARTUP_DIR=%IPYTHON_PROFILE_PATH%\startup
if not exist "%STARTUP_DIR%" (
    mkdir "%STARTUP_DIR%"
)

copy ".pythonrc.py" "%STARTUP_DIR%\"

REM Step 3: Add the full path of .pythonrc.py to PYTHONSTARTUP environment variable for the current user
set PYTHONRC_PATH=%STARTUP_DIR%\.pythonrc.py
setx PYTHONSTARTUP "%PYTHONRC_PATH%" /m

echo Successfully added .pythonrc.py to IPython startup and PYTHONSTARTUP environment variable.
pause
