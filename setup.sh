#!/bin/bash

echo "Setting up AetherShell environment..."

# 1. Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# shellcheck source=/dev/null
source venv/bin/activate

# 2. Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# 3. Install Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

# 4. Create model folder
echo "Creating models directory..."
mkdir -p models

# 5. Download model if not already present
MODEL_NAME="mistral-7b-instruct-v0.1.Q4_K_M.gguf"
MODEL_PATH="models/$MODEL_NAME"
MODEL_URL="https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/$MODEL_NAME"

if [ ! -f "$MODEL_PATH" ]; then
    echo "Downloading Mistral model..."
    curl -L "$MODEL_URL" -o "$MODEL_PATH"
else
    echo "Model already exists at $MODEL_PATH"
fi

# 6. Done
echo ""
echo "Setup complete."
echo "To start using AetherShell:"
echo "  source venv/bin/activate"
echo "  python assistant.py"
