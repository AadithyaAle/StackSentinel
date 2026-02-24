# 🛡️ StackSentinel

**An Autonomous, Self-Healing Linux Infrastructure Agent powered by Amazon Nova.**

## 📑 Index

1. [Overview](https://www.google.com/search?q=%23overview)
2. [Key Features](https://www.google.com/search?q=%23key-features)
3. [Prerequisites](https://www.google.com/search?q=%23prerequisites)
4. [Installation & Setup](https://www.google.com/search?q=%23installation--setup)
5. [Usage Guide](https://www.google.com/search?q=%23usage-guide)
6. [Full CLI Command Reference](https://www.google.com/search?q=%23full-cli-command-reference)
7. [Teardown & Uninstallation](https://www.google.com/search?q=%23teardown--uninstallation)
8. [License](https://www.google.com/search?q=%23license)

## 🚀 Overview

System administrators cannot monitor terminal outputs 24/7. **StackSentinel** is a lightweight, edge-deployed AI watchdog that actively monitors Linux system logs, diagnoses critical hardware and software faults in real-time, and securely executes autonomous bash commands to heal the system before a total crash occurs.

Coupled with a mobile-responsive Command and Control (C2) dashboard, admins get live system telemetry and remote lockdown capabilities right from their phones.

## ✨ Key Features

* **🧠 LLM-Powered Remediation:** Integrates with AWS Bedrock (Amazon Nova) to diagnose raw system logs and generate precise bash fixes.
* **🛡️ Execution Safety Net:** A multi-layered guardrail system that intercepts AI-generated scripts to block destructive commands (like `rm -rf` or `mkfs`) and enforces 15-second execution timeouts.
* **🔒 Command Auditor:** An additional logic layer that cross-references suggested fixes against system security policies.
* **⚡ Crash-Proof IPC:** Engineered with atomic JSON file writes and global `0o666` permissions to ensure seamless communication between the Root Watchdog and the User-level C2 Dashboard.
* **🌐 Auto-Tunneling C2:** Integrated `pyngrok` support that automatically generates a public URL for your dashboard on startup.

## ⚠️ Prerequisites

To run StackSentinel locally, you must have:

1. A Linux/macOS environment (Windows requires WSL).
2. An active AWS Account with access to the **Amazon Nova 2 Lite** model in Bedrock.
3. AWS CLI configured with your SSO or IAM credentials (`aws configure sso`).

## 💻 Installation & Setup

Developed and stress-tested on Ubuntu Linux. We provide an automated installation script that securely sets up the Python virtual environment to protect your system packages and installs the StackSentinel CLI tools.

**1. Clone & Navigate**

```bash
git clone https://github.com/AadithyaAle/StackSentinel.git
cd StackSentinel

```

**2. Run the Installer**

```bash
chmod +x install.sh uninstall.sh
./install.sh

```

**3. AWS Authentication**
Ensure you are logged into your secure AWS profile:

```bash
aws sso login --profile Stack-Sentinel

```

**4. Ngrok Authentication (For the Web UI)**
To use the automated public dashboard tunnel, you must link your free Ngrok account:

```bash
ngrok config add-authtoken YOUR_NGROK_TOKEN

```

## 🎮 Usage Guide

> [!IMPORTANT]
> **Virtual Environment Isolation:** Because StackSentinel installs into a safe virtual environment to protect your system, you **must activate it** before running the global commands.

**Step 1: Activate the Environment & Start the Web Dashboard**
Open your terminal, navigate to the StackSentinel directory, and run:

```bash
source venv/bin/activate
stacksentinel-ui

```

*The public Ngrok URL will be printed directly in your terminal so you can open it on your phone.*

**Step 2: Arm the Watchdog**
Open a second terminal window, activate the environment again, and start the agent.

*Note: To allow the AI to fix system-level issues while maintaining access to your AWS credentials, you must use the `-E` flag with `sudo`. This preserves your environment variables so the AI can "think" while having the power to "act."*

```bash
source venv/bin/activate
sudo -E stacksentinel --watchdog

```

**Step 3: Test the Auto-Healing (Simulation)**
To safely test the AI's execution capabilities, open a third terminal and inject a harmless missing-directory error into the log file:

```bash
echo "CRITICAL: Nginx failed to start. The required cache directory /tmp/stacksentinel_cache does not exist." >> /tmp/stacksentinel_dummy_log.txt

```

Watch your terminal or phone dashboard as the AI intercepts the log, consults Amazon Nova, audits the `mkdir` command for safety, and physically creates the directory on your machine.

## 🧰 Full CLI Command Reference

StackSentinel is highly modular. You can use it as a passive monitor, an active guardian, or an interactive educational tool.

| Command | Description |
| --- | --- |
| `stacksentinel "error"` | **Standard Mode:** Manually ask the AI to diagnose a specific error. |
| `sudo -E stacksentinel --watchdog` | **Active Defense:** Runs the continuous AFK protection and auto-healing loop. |
| `stacksentinel --watch` | **Passive Defense:** Monitors logs without executing fixes. |
| `stacksentinel --gym` | **Training:** Enter the interactive threat-response training simulator. |
| `stacksentinel --learn "error"` | **Professor Mode:** Explains Linux concepts before showing the fix. |
| `stacksentinel --teach` | **Feedback:** Provide manual corrections to the AI. |
| `stacksentinel --report` | **Analytics:** View the AI's success/failure performance score. |
| `stacksentinel --history` | **Audit Trail:** View a color-coded log of every command executed. |
| `stacksentinel --snapshot` | **Backups:** Create an instant JSON state backup of the system. |
| `stacksentinel --restore` | **Rollback:** Revert to a previous system snapshot. |
| `stacksentinel --set-baseline` | **Security:** Set a known-good configuration baseline. |
| `stacksentinel --audit` | **Security:** Check for unauthorized configuration drift. |

## 🗑️ Teardown & Uninstallation

To completely remove the StackSentinel CLI tools and isolated virtual environment from your system, simply run the included uninstaller:

```bash
./uninstall.sh

```

## 🤝 Open Source

This project explores the intersection of AI inference and low-level systems engineering.

---

**License:** MIT

---
