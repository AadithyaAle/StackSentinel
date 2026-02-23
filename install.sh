#!/bin/bash

echo "🚀 Initiating StackSentinel Installation..."

# Get exact paths
APP_DIR=$(pwd)
CURRENT_USER=$(whoami)

echo "📦 Setting up Python Virtual Environment..."
python3 -m venv venv
source venv/bin/activate

echo "📥 Installing dependencies and native CLI tools..."
pip install -r requirements.txt
pip install .

echo "⚙️ Configuring systemd background daemon..."
SERVICE_CONTENT="[Unit]
Description=StackSentinel AI Autonomous Watchdog
After=network.target

[Service]
User=$CURRENT_USER
WorkingDirectory=$APP_DIR
ExecStart=$APP_DIR/venv/bin/stacksentinel --watchdog
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target"

echo "$SERVICE_CONTENT" > stacksentinel.service
sudo mv stacksentinel.service /etc/systemd/system/

echo "🔄 Reloading Linux daemons..."
sudo systemctl daemon-reload
sudo systemctl enable stacksentinel
sudo systemctl restart stacksentinel

echo "✅ Installation Complete! The daemon is running in the background."
