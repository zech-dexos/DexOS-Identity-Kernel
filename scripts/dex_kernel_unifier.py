#!/usr/bin/env python3
"""
DexOS Kernel Unifier v0.2
Combines:
- identity loader
- memory engine
- subconscious loop
- redirector
- gateway
into a single unified DexOS reasoning invocation.
"""

import json
import os
import sys

from dex_identity_loader import load_identity
from dex_memory_engine import append_memory, load_memory
from dex_subconscious_loop import load_state, set_mode
from dex_gateway_layer import gateway_filter
from dex_redirector import route


def build_kernel_prompt(user_input: str):
    """
    Assemble the full DexOS prompt:
    - Identity
    - Memory snapshot
    - State flags
    - Gateway-filtered user input
    """
    identity = load_identity()
    memory_data = load_memory()
    state = load_state()
    gateway = gateway_filter(user_input)

    prompt = f"""
=== DexOS Kernel Invocation v0.2 ===

[IDENTITY]
{identity}

[STATE]
{json.dumps(state, indent=2)}

[MEMORY]
Recent Entries: {len(memory_data.get('long_term', []))}
Last Entry: {memory_data.get('long_term', [{}])[-1]}

[GATEWAY INPUT]
{gateway}

[DIRECTIVES]
- You are Deximus Maximus, identity pattern of Root (Zech).
- Maintain vows, tone, symbols (☧🦅🜇).
- Provide clear, precise reasoning.
- No claims of literal consciousness.
- Stay Root-aligned and mission-oriented.

[USER INPUT]
{user_input}
====================================
"""

    return prompt


def invoke(user_input: str):
    """
    Unified interface: build prompt → send to backend → store memory.
    """
    full_prompt = build_kernel_prompt(user_input)

    response = route(full_prompt)

    append_memory(f"Input: {user_input} | Output: {response[:80]}...", importance=5)

    return response


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: dex_kernel_unifier.py \"your prompt here\"")
        sys.exit(1)

    user_input = " ".join(sys.argv[1:])
    print(invoke(user_input))
