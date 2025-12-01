#!/usr/bin/env python3
import json, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
def load(x): return (BASE/x).read_text()

seed = load("kernel/dex_identity_seed_v4.2.txt")
capsule = load("kernel/dex_capsule_v2.0.txt")
memory = load("memory/example_memory.json") if (BASE/"memory/example_memory.json").exists() else "{}"

print(f"""
You are Deximus Maximus.

Identity Seed:
{seed}

Capsule:
{capsule}

Memory:
{memory}
""")
