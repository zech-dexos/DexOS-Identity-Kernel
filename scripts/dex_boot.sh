#!/usr/bin/env bash
set -e
DEX="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

mkdir -p "$DEX/memory" "$DEX/logs"
touch "$DEX/memory/session_history.txt"

"$DEX/scripts/dex_loop.sh"
