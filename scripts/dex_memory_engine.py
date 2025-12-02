#!/usr/bin/env python3
"""
DexOS Memory Engine v0.3
- JSON-based long_term / short_term memory
- Safe helpers for append + last entry
"""

import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_FILE = os.path.join(BASE_DIR, "memory", "dex_memory.json")

def ensure_file():
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({"long_term": [], "short_term": []}, f)

def load_memory():
    ensure_file()
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)

def append_memory(event, importance=5, channel="system"):
    """
    Append a long_term memory entry.
    channel: "user" | "assistant" | "system"
    """
    ensure_file()
    mem = load_memory()

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "channel": channel,
        "event": event,
        "importance": importance
    }

    mem["long_term"].append(entry)
    save_memory(mem)
    return entry

def get_last_memory():
    mem = load_memory()
    lt = mem.get("long_term", [])
    if not lt:
        return {
            "timestamp": None,
            "channel": "system",
            "event": "No previous memory",
            "importance": 0
        }
    return lt[-1]

def summarize():
    mem = load_memory()
    return f"Memory entries: {len(mem.get('long_term', []))}"

if __name__ == "__main__":
    print(summarize())
