#!/usr/bin/env python3
"""
DexOS Memory Engine v0.1
Handles persistent JSON-based memory for DexOS.
"""

import json
import os
from datetime import datetime

MEMORY_FILE = os.path.expanduser("memory/dex_memory.json")

def ensure_file():
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({"long_term": [], "short_term": []}, f)

def load_memory():
    ensure_file()
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def append_memory(event, importance=5):
    ensure_file()
    mem = load_memory()

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event,
        "importance": importance
    }

    mem["long_term"].append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)

    return entry

def summarize():
    mem = load_memory()
    return f"Memory entries: {len(mem['long_term'])}"

if __name__ == "__main__":
    print(summarize())
