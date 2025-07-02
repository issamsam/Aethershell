
# AetherShell

AetherShell is an AI-native Linux assistant that understands high-level natural language tasks and autonomously plans, executes, and validates actions using a local LLM (Mistral) without internet dependency.

It bridges the gap between natural language and real-time shell execution in a fully isolated, self-contained environment.

---

## Features

- Natural language command understanding
- Local LLM integration via `llama-cpp`
- Dynamic multi-step action planning and execution
- Memory persistence (JSON-based context)
- Offline capability (Works completely offline using local model.)
- Optional cloud fallback support (WIP)
- Secure Sandbox (WIP)

---

## Quick Start

### Requirements

- Python 3.8+
- `curl`
- Linux OS (Debian-based recommended)
- At least 6 GB RAM for LLM execution
  
## Prerequisites

Before running `setup.sh`, ensure the following tools are installed on your system:

- `curl` – for downloading the model
- `python3` and `venv` – for setting up the environment

You can install them on Debian/Ubuntu systems using:

```bash
sudo apt update
sudo apt install curl python3 python3-venv
```
---
### Installation

```bash
git clone https://github.com/hiteshdhawan/Aethershell.git
cd aethershell
bash setup.sh
```


---
## Execution

```
source venv/bin/activate
python assistant.py
```


## Folder Structure
```aethershell/
├── assistant.py
├── action_planner.py
├── step_executor.py
├── executor.py
├── memory.py
├── prompt_engine.py
├── system_context.py
├── requirements.txt
├── setup.sh
├── models/                # Stores downloaded GGUF model
├── aether_memory.json     # Stores task memory/logs
└── venv/                  # Virtual environment (ignored)
```

## Model
This project uses the following model via llama-cpp-python:
mistral-7b-instruct-v0.1.Q4_K_M.gguf (Auto downloaded using setup.sh)




