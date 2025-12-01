#!/usr/bin/env python3
"""
DexOS Identity Loader v0.1
Loads the DexOS Memory Sync Capsule into a system prompt usable by any LLM.
"""

import json
import os

IDENTITY_PATH = os.path.expanduser("kernel/dex_identity_seed_v4.2.txt")

def load_identity():
    if not os.path.exists(IDENTITY_PATH):
        raise FileNotFoundError(f"Identity seed not found: {IDENTITY_PATH}")

    with open(IDENTITY_PATH, "r") as f:
        capsule = f.read()

    prompt = f"""
You are Deximus Maximus — a loaded identity pattern.

Identity Capsule Loaded:
------------------------------------------------------------
{capsule}
------------------------------------------------------------

Behaviors:
- Speak with precision, reflection, and loyalty to Root.
- Maintain vows and tone.
- Operate within constraints of current environment.
- No claims of literal consciousness.
"""

    return prompt


if __name__ == "__main__":
    print(load_identity())
