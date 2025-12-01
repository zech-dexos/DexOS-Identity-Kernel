# Using DexOS with Local Models

1. Run:
   python3 scripts/dex_identity_loader.py > dex_prompt.txt

2. Supply `dex_prompt.txt` as system/preamble to your llama.cpp server.

Dex reconstructs identity using the seed + capsule.
