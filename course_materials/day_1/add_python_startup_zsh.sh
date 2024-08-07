#!/bin/zsh

# Step 1: Create IPython profile if not existing
ipython profile create

# Get the IPython profile directory
IPYTHON_PROFILE_PATH=$(ipython locate profile)

# Step 2: Copy .pythonrc.py file to the startup folder under the IPython profile
STARTUP_DIR="$IPYTHON_PROFILE_PATH/startup"
mkdir -p "$STARTUP_DIR"

if [ -f ".pythonrc.py" ]; then
    cp ".pythonrc.py" "$STARTUP_DIR/"
else
    echo ".pythonrc.py file not found in the current directory."
    exit 1
fi

# Step 3: Add the full path of .pythonrc.py to PYTHONSTARTUP environment variable for the current user
PYTHONRC_PATH="$STARTUP_DIR/.pythonrc.py"
if grep -q "export PYTHONSTARTUP=" ~/.zshrc; then
    sed -i '' "s|export PYTHONSTARTUP=.*|export PYTHONSTARTUP=\"$PYTHONRC_PATH\"|g" ~/.zshrc
else
    echo "export PYTHONSTARTUP=\"$PYTHONRC_PATH\"" >>~/.zshrc
fi

source ~/.zshrc

echo "Successfully added .pythonrc.py to IPython startup and PYTHONSTARTUP environment variable."
