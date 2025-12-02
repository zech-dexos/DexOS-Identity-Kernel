#!/usr/bin/env bash
# DexOS Runtime Launcher v0.2

echo "== DexOS Runtime =="

# Load Identity
echo "[1/4] Loading identity..."
python3 scripts/dex_identity_loader.py > runtime_identity_prompt.txt

# Memory
echo "[2/4] Checking memory..."
python3 scripts/dex_memory_engine.py

# Reflex
echo "[3/4] Initializing reflex engine..."
python3 scripts/dex_reflex_engine.py

# Subconscious State
echo "[4/4] Subconscious state:"
python3 scripts/dex_subconscious_loop.py

echo "DexOS runtime v0.2 initialized."
