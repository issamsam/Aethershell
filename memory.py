import json
import os

MEMORY_FILE = "aether_memory.json"

def remember(task, result):
    memory_log = recall_all()
    memory_log.append({"task": task, "result": result})
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_log, f, indent=2)

def recall_all():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def clear_memory():
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
