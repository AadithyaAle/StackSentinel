# 🛡️ StackSentinel

[![Python 3](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock%20Nova-orange.svg)](https://aws.amazon.com/bedrock/)
[![Flask](https://img.shields.io/badge/Web-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**An Autonomous, Self-Healing Linux Infrastructure Agent powered by Amazon Nova.**

## 📑 Index
1. [Overview](#-overview)
2. [Key Features](#-key-features)
3. [Installation & Setup](#-installation--setup)
4. [Usage Guide](#-usage-guide)
5. [Advanced CLI Capabilities](#-advanced-cli-capabilities)
6. [License](#-license)

## 🚀 Overview

System administrators cannot monitor terminal outputs 24/7. **StackSentinel** is a lightweight, edge-deployed AI watchdog that actively monitors Linux system logs, diagnoses critical hardware and software faults in real-time, and securely executes autonomous bash commands to heal the system before a total crash occurs. 

Coupled with a mobile-responsive Command and Control (C2) dashboard, admins get live system telemetry and remote lockdown capabilities right from their phones.

## ✨ Key Features

* **🧠 LLM-Powered Remediation:** Integrates with AWS Bedrock (Amazon Nova) to diagnose raw system logs and generate precise bash fixes.
* **🔒 Command Auditor:** A strict safety layer that intercepts AI-generated scripts to block dangerous commands like `rm -rf`.
* **⚡ Crash-Proof IPC:** Engineered with atomic JSON file writes to ensure the Watchdog and C2 server communicate without system lag.
* **🌐 Auto-Tunneling C2:** Integrated `pyngrok` support that automatically generates a public URL for your dashboard on startup.

## 💻 Installation & Setup

Developed and stress-tested on Ubuntu Linux. We provide an automated installation script that sets up the Python virtual environment and installs the StackSentinel global CLI tools.

**1. Clone & Navigate**
```bash
git clone [https://github.com/YOUR_USERNAME/StackSentinel.git](https://github.com/YOUR_USERNAME/StackSentinel.git)
cd StackSentinel

```

**2. Run the Installer**

```bash
chmod +x install.sh
./install.sh

```

**3. AWS Authentication**
Ensure you are logged into your secure AWS profile:

```bash
aws sso login --profile Stack-Sentinel

```

## 🎮 Usage Guide

Thanks to the automated CLI setup, you can run StackSentinel from **any** terminal directory on your machine. We enforce a "User-Intended" security model, meaning the autonomous agent only runs when you explicitly arm it.

**Step 1: Start the Web Dashboard**
Open any terminal and run:

```bash
stacksentinel-ui

```

*The public Ngrok URL will be printed directly in your terminal so you can open it on your phone.*

**Step 2: Arm the Watchdog**
When you are ready to authorize the AI to guard your system, open a new terminal and explicitly arm the agent:

```bash
stacksentinel --watchdog

```

**Step 3: Test the Auto-Healing (Simulation)**
To safely test the AI's execution capabilities, open a third terminal and inject a harmless missing-directory error into the log file:

```bash
cd StackSentinel
echo "CRITICAL: Backup service failed. Directory /tmp/stacksentinel_test missing." >> system_log.txt

```

Watch your terminal or phone dashboard as the AI intercepts the log, consults Amazon Nova, audits the `mkdir` command for safety, and physically creates the directory on your machine.

## 🧰 Full CLI Command Reference

StackSentinel is highly modular. You can use it as a background daemon, a passive monitor, or an interactive educational tool.

| Command | Description |
| :--- | :--- |
| `stacksentinel "error message"` | **Standard Mode:** Manually ask the AI to diagnose a specific error. |
| `stacksentinel --watchdog` | **Active Defense:** Runs the continuous AFK protection and auto-healing loop. |
| `stacksentinel --watch` | **Passive Defense:** Monitors and displays logs continuously without executing fixes. |
| `stacksentinel --gym` | **Training:** Enter the interactive threat-response training simulator. |
| `stacksentinel --learn "error"` | **Professor Mode:** Explains Linux concepts before showing the fix. |
| `stacksentinel --teach` | **Feedback:** Provide manual corrections to the AI to improve future responses. |
| `stacksentinel --report` | **Analytics:** View the AI's success/failure performance score. |
| `stacksentinel --history` | **Audit Trail:** View a color-coded log of every command the AI has executed. |
| `stacksentinel --snapshot` | **Backups:** Create an instant JSON state backup of the system. |
| `stacksentinel --restore` | **Rollback:** Open the interactive menu to revert to a previous snapshot. |
| `stacksentinel --set-baseline`| **Security:** Set a known-good configuration baseline for the OS. |
| `stacksentinel --audit` | **Security:** Check for unauthorized configuration drift against the baseline. |

## 🤝 Open Source

This project explores the intersection of AI inference and low-level systems engineering. Built for the Hackathon with ❤️.

---

**License:** MIT

