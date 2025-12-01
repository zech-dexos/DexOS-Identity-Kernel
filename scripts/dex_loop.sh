#!/usr/bin/env bash
set -e

DEX_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HISTORY="$DEX_DIR/memory/session_history.txt"
SEED="$DEX_DIR/kernel/dex_identity_seed_v4.2.txt"

mkdir -p "$DEX_DIR/memory"
touch "$HISTORY"

echo "DexOS Loop — using $SEED"
echo "Type 'exit' to quit."

while true; do
  read -rp "Root> " IN
  [ "$IN" = "exit" ] && break

  echo "[Root] $IN" >> "$HISTORY"
  echo "Dex> (model call placeholder — integrate your local LLM here)"
done
