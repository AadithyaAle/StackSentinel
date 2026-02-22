import os
import json
import threading
import requests
import subprocess
from rich.console import Console

console = Console()
SETTINGS_FILE = "settings.json"

# --- CONFIGURATION ---
# 1. Go to your Discord Server -> Channel Settings -> Integrations -> Webhooks
# 2. Paste the URL below (Leave empty to disable)
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK", "") 

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {"enable_desktop_notifications": True}
    try:
        with open(SETTINGS_FILE, "r") as f: return json.load(f)
    except: return {}

def _send_discord_payload(payload):
    """
    Internal function to push to Discord. 
    Runs in a thread to prevent blocking the Main Watchdog Loop.
    """
    if not DISCORD_WEBHOOK_URL: return
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=3)
    except Exception:
        pass # Fail silently if internet is down (Anti-Crash)

def send_alert(title, message, urgency="normal"):
    """
    The Universal Alert System.
    Sends to: Desktop Notification (Notify-Send) AND Discord.
    """
    # 1. Desktop Notification (Linux)
    settings = load_settings()
    if settings.get("enable_desktop_notifications", True):
        try:
            icon = "dialog-error" if urgency == "critical" else "dialog-information"
            # Use specific urgency level for Linux
            linux_urgency = "critical" if urgency == "critical" else "normal"
            subprocess.Popen(["notify-send", "-u", linux_urgency, "-i", icon, title, message])
        except FileNotFoundError:
            pass

    # 2. Discord Webhook (Cloud)
    if DISCORD_WEBHOOK_URL:
        color = 15158332 if urgency == "critical" else 3066993 # Red vs Green
        payload = {
            "username": "StackSentinel Agent",
            "avatar_url": "https://i.imgur.com/4M34hi2.png",
            "embeds": [{
                "title": f"🛡️ {title}",
                "description": message,
                "color": color
            }]
        }
        # Run in background thread so we NEVER freeze the main app
        threading.Thread(target=_send_discord_payload, args=(payload,), daemon=True).start()

def send_startup_ping():
    send_alert("System Online", "StackSentinel Watchdog has been armed.", "normal")