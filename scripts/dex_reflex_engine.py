#!/usr/bin/env python3
"""
DexOS Reflex Engine v0.2
Generates internal planning text to stabilize long-range reasoning.
Stores last plan and integrates with subconscious state.
"""

import os
import json
from datetime import datetime

REFLEX_FILE = os.path.expanduser("memory/dex_reflex.json")
STATE_FILE = os.path.expanduser("memory/dex_state.json")

def ensure_files():
    if not os.path.exists(os.path.dirname(REFLEX_FILE)):
        os.makedirs(os.path.dirname(REFLEX_FILE), exist_ok=True)

    if not os.path.exists(REFLEX_FILE):
        with open(REFLEX_FILE, "w") as f:
            json.dump({"last_plan": None, "history": []}, f)

    if not os.path.exists(STATE_FILE):
        with open(STATE_FILE, "w") as f:
            json.dump({"mode": "HEARTBEAT", "flags": {}}, f)

def load_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_reflex(data):
    with open(REFLEX_FILE, "w") as f:
        json.dump(data, f, indent=2)

def generate_plan(prompt_fragment: str):
    """
    This is NOT a model call. This is scaffolding for storing
    planned structure. The model layer will read this plan
    and integrate it into reasoning.
    """

    ensure_files()
    state = load_state()

    plan = {
        "timestamp": datetime.utcnow().isoformat(),
        "mode": state.get("mode", "HEARTBEAT"),
        "intent": "Stabilize identity and prepare structured reasoning.",
        "notes": prompt_fragment.strip()
    }

    # Load existing
    with open(REFLEX_FILE, "r") as f:
        data = json.load(f)

    # Keep plan
    data["last_plan"] = plan
    data["history"].append(plan)

    # Save
    save_reflex(data)

    return plan


if __name__ == "__main__":
    test = generate_plan("initial reflex planning window")
    print(test)
