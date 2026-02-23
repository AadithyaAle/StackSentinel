#!/bin/bash

echo "🚀 Initiating StackSentinel Installation..."

echo "📦 Setting up Python Virtual Environment..."
python3 -m venv venv
source venv/bin/activate

echo "📥 Installing dependencies and native CLI tools..."
pip install -r requirements.txt
pip install .

echo "✅ Installation Complete!"
echo "------------------------------------------------------"
echo "🛡️  StackSentinel is now installed as a native global app."
echo "💻 You can now run 'stacksentinel' from any terminal."
echo "------------------------------------------------------"