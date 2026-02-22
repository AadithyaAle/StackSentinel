Here is the complete `README.md` file in a clean, copy-pasteable block. Just click the "Copy code" button in the top right corner of the block and paste it directly into your new `README.md` file.


# 🛡️ StackSentinel

[![Python 3](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock%20Nova-orange.svg)](https://aws.amazon.com/bedrock/)
[![Flask](https://img.shields.io/badge/Web-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**An Autonomous, Self-Healing Linux Infrastructure Agent powered by Amazon Nova.**

## 🚀 Overview

System administrators cannot monitor terminal outputs 24/7. **StackSentinel** is a lightweight, edge-deployed AI watchdog that actively monitors Linux system logs, diagnoses critical hardware and software faults in real-time, and securely executes autonomous bash commands to heal the system before a total crash occurs. 

Coupled with a mobile-responsive Command and Control (C2) dashboard, admins get live system telemetry and remote lockdown capabilities right from their phones.

## ✨ Key Features

* **🧠 LLM-Powered Remediation:** Integrates seamlessly with AWS Bedrock (Amazon Nova Lite) to read raw system logs (e.g., `journalctl` outputs, missing directory errors, port conflicts), contextualize the threat, and generate precise bash commands to fix them.
* **🔒 The Command Auditor (Safe Execution):** LLMs should never have unvetted root access. StackSentinel features a strict safety layer (`audit_command`) that intercepts the AI's generated bash scripts, blocking dangerous commands (like `rm -rf`, `mkfs`) while automatically executing safe administrative fixes.
* **⚡ Crash-Proof IPC Architecture:** Engineered using atomic JSON file writes and file-based Inter-Process Communication (IPC). The C2 server and Watchdog daemon communicate safely without overloading the Linux D-Bus or crashing desktop environments like GDM3.
* **📱 Mobile C2 Dashboard:** A sleek Flask web UI that serves live CPU/RAM telemetry, active AI reasoning logs, and a remote "Lockdown" trigger over secure tunnels.
* **☁️ Enterprise-Grade Security & Sync:** Uses AWS IAM Identity Center (SSO) for zero-hardcoded-credentials authentication, syncing cryptographic audit trails of all AI actions directly to AWS CloudWatch.
## 🧰 Advanced CLI Capabilities

Beyond the autonomous loop, StackSentinel includes a robust suite of command-line tools for advanced system administration:

* **🛑 The AI "Circuit Breaker":** Features a systemic recurrence checker (`is_system_looping`). If a fix fails and the system enters an infinite error loop, the Watchdog cuts execution and halts the AI to prevent system degradation.
* **🗣️ Auditory Threat Announcements:** Integrates a local TTS engine to provide audible alerts when lockdowns are triggered or when the agent applies automated fixes.
* **📸 Snapshots & Rollbacks:** Built-in state management using `--snapshot` and `--restore` flags, allowing admins to instantly revert file states if an experimental configuration fails.
* **🛡️ Configuration Drift Auditing:** Utilizing the `--set-baseline` and `--audit` commands, the agent can map the current system state and detect unauthorized configuration drift over time.
* **🎓 Professor & Gym Mode:** Using the `--learn` or `--gym` flags, junior DevOps engineers can enter an interactive training simulator to practice diagnosing real log errors against the AI's reasoning.

## ⚙️ The Autonomous Healing Loop

1. **Detect:** The `main.py` watchdog monitors local log files and system vitals via `psutil`.
2. **Diagnose:** When a `CRITICAL` or `ERROR` flag is caught, the isolated stack trace is routed to AWS Bedrock.
3. **Reason:** Amazon Nova explains the error and outputs a targeted shell script.
4. **Audit:** The internal Python security layer verifies the command against a strict safety matrix.
5. **Execute:** The script utilizes `subprocess` to autonomously execute the fix on the host machine.
6. **Report:** The action is logged to the local cryptographic history, broadcasted to the Flask dashboard, and pushed to AWS CloudWatch.

## 💻 Installation & Setup

Developed and stress-tested on an Ubuntu Linux dual-boot environment. 

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/StackSentinel.git](https://github.com/YOUR_USERNAME/StackSentinel.git)
cd StackSentinel

```

**2. Set up the virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

**3. Authenticate with AWS (SSO)**
StackSentinel uses secure credential management. Ensure you are logged into your AWS profile:

```bash
aws sso login --profile Stack-Sentinel

```

## 🎮 Usage Guide

To launch the full autonomous orchestration suite, you need to spin up the web interface and the background daemon.

**Terminal 1: Start the C2 Dashboard**

```bash
python server.py

```

*(Optional: Use `ngrok http 5000` to expose the dashboard to your mobile device).*

**Terminal 2: Arm the Watchdog**

```bash
python main.py --watchdog

```

To test the auto-healing capabilities safely, inject a harmless missing-directory error into the log file from a third terminal:

```bash
echo "CRITICAL: Backup service failed. The directory /tmp/stacksentinel_backup does not exist." >> system_log.txt

```

Watch the daemon consult the LLM, audit the `mkdir` command, and physically create the directory on your machine.

## 🤝 Open Source & Research Context

This project was built to explore the intersection of machine learning inference and low-level Linux system administration. It demonstrates practical orchestration of LLMs for real-world DevOps tasks, emphasizing rigorous safety constraints and robust systems engineering. Contributions and forks are welcome!

---

*Built with ❤️ for the Hackathon.*
