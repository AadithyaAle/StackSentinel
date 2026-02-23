This is the final touch to make your repository look like a professional, enterprise-grade tool. I have updated the **Installation** and **Usage** sections to reflect your new native CLI commands (`stacksentinel` and `stacksentinel-ui`) and included the `pip install .` step.

I also added your dynamic index back at the top so it's easy to navigate!

### 🛡️ Updated `README.md`

```markdown
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
6. [The Autonomous Healing Loop](#-the-autonomous-healing-loop)
7. [License](#-license)

## 🚀 Overview

System administrators cannot monitor terminal outputs 24/7. **StackSentinel** is a lightweight, edge-deployed AI watchdog that actively monitors Linux system logs, diagnoses critical hardware and software faults in real-time, and securely executes autonomous bash commands to heal the system before a total crash occurs. 

Coupled with a mobile-responsive Command and Control (C2) dashboard, admins get live system telemetry and remote lockdown capabilities right from their phones.

## ✨ Key Features

* **🧠 LLM-Powered Remediation:** Integrates with AWS Bedrock (Amazon Nova) to diagnose raw system logs and generate precise bash fixes.
* **🔒 Command Auditor:** A strict safety layer that intercepts AI-generated scripts to block dangerous commands like `rm -rf`.
* **⚡ Crash-Proof IPC:** Engineered with atomic JSON file writes to ensure the Watchdog and C2 server communicate without system lag.
* **🌐 Auto-Tunneling C2:** Integrated `pyngrok` support that automatically generates a public URL for your dashboard on startup.

## 💻 Installation & Setup

Developed and stress-tested on Ubuntu Linux. 

**1. Clone & Navigate**
```bash
git clone [https://github.com/YOUR_USERNAME/StackSentinel.git](https://github.com/YOUR_USERNAME/StackSentinel.git)
cd StackSentinel

```

**2. Environment & Dependencies**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

**3. Install Native CLI Commands**
This step registers `stacksentinel` as a global command on your system.

```bash
pip install .

```

**4. AWS Authentication**

```bash
aws sso login --profile Stack-Sentinel

```

## 🎮 Usage Guide

Thanks to our automated CLI setup, you no longer need to type `python main.py`. You can run these commands from **any** terminal directory.

**Step 1: Start the Web Dashboard**

```bash
stacksentinel-ui

```

*The public Ngrok URL will be printed directly in your terminal.*

**Step 2: Arm the Watchdog**

```bash
stacksentinel --watchdog

```

**Step 3: Test the Healing (Simulation)**
Inject a missing-directory error into your log:

```bash
echo "CRITICAL: Backup service failed. Directory /tmp/stacksentinel_test missing." >> system_log.txt

```

## 🧰 Advanced CLI Reference

| Command | Description |
| --- | --- |
| `stacksentinel --gym` | Enter the interactive threat-response training simulator. |
| `stacksentinel --learn "error"` | Professor Mode: Explains Linux concepts before showing the fix. |
| `stacksentinel --snapshot` | Create an instant backup of the current system state. |
| `stacksentinel --restore` | Open the interactive menu to roll back to a previous state. |
| `stacksentinel --history` | View a color-coded audit trail of every AI action taken. |
| `stacksentinel --audit` | Check for configuration drift against your set baseline. |

## 🤝 Open Source

This project explores the intersection of AI inference and low-level systems engineering. Built for the Hackathon with ❤️.

---

**License:** MIT

```