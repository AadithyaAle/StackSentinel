#!/bin/bash

echo "🗑️ Removing StackSentinel daemon..."
sudo systemctl stop stacksentinel
sudo systemctl disable stacksentinel
sudo rm /etc/systemd/system/stacksentinel.service
sudo systemctl daemon-reload

echo "✅ StackSentinel has been safely uninstalled from systemd."
