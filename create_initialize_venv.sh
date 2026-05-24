#!/bin/bash

# Define the name of the virtual environment folder
VENV_NAME=".venv"

# 1. Create the virtual environment if it doesn't exist
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment: $VENV_NAME..."
    python3 -m venv $VENV_NAME
else
    echo "Virtual environment already exists."
fi

# 2. Activate the environment
# Note: To keep it active in your current terminal, you must 'source' this script
source $VENV_NAME/bin/activate

# 3. Upgrade pip and install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "No requirements.txt found. Skipping installation."
fi

echo "Environment is ready!"