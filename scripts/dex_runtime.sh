#!/usr/bin/env bash
# DexOS Runtime v0.3 — quick status check

echo "== DexOS Runtime v0.3 =="

echo "[1/3] Memory summary:"
python3 scripts/dex_memory_engine.py

echo
echo "[2/3] Subconscious state:"
python3 scripts/dex_subconscious_loop.py

echo
echo "[3/3] Kernel sample:"
python3 scripts/dex_kernel_unifier.py | head -n 40
