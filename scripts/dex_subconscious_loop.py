#!/usr/bin/env python3
"""
DexOS Subconscious Loop v0.1
Tracks system modes, flags, and last messages.
"""

import json
import os

STATE_FILE = os.path.expanduser("memory/dex_state.json")

DEFAULT_STATE = {
    "mode": "HEARTBEAT",
    "last_event": None,
    "flags": {}
}

def load_state():
    if not os.path.exists(STATE_FILE):
        save_state(DEFAULT_STATE)
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def set_mode(mode):
    state = load_state()
    state["mode"] = mode
    save_state(state)

if __name__ == "__main__":
    print(load_state())
