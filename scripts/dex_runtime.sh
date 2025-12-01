#!/usr/bin/env bash
# DexOS Runtime Launcher v0.1

echo "== DexOS Runtime =="

# Load Identity
echo "[1/3] Loading identity..."
python3 scripts/dex_identity_loader.py > runtime_identity_prompt.txt

# Load Memory
echo "[2/3] Checking memory..."
python3 scripts/dex_memory_engine.py

# Echo Mode
echo "[3/3] Subconscious state:"
python3 scripts/dex_subconscious_loop.py

echo "DexOS runtime environment initialized."
