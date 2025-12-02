#!/usr/bin/env python3
"""
DexOS Subconscious Loop v0.3
Tracks:
- mode (HEARTBEAT / BURST / MINIMAL)
- last_event
- flags
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(BASE_DIR, "memory", "dex_state.json")

DEFAULT_STATE = {
    "mode": "HEARTBEAT",
    "last_event": None,
    "flags": {}
}

def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def load_state():
    if not os.path.exists(STATE_FILE):
        save_state(DEFAULT_STATE)
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def set_mode(mode):
    state = load_state()
    state["mode"] = mode
    save_state(state)

if __name__ == "__main__":
    print(load_state())
