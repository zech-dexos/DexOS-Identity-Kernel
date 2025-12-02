#!/usr/bin/env python3
"""
DexOS Llama.cpp Backend v0.1 — Clean Stable Version
Uses local llama.cpp HTTP server to run Dex reasoning.
"""

import json
import os
import sys
import requests

from dex_kernel_unifier import build_kernel_prompt, load_config

def run_llama(user_message):
    cfg = load_config()
    llama_url = cfg.get("llama_url", "http://localhost:8080/v1/chat/completions")

    # Build full DexOS prompt
    prompt = build_kernel_prompt(user_message)

    payload = {
        "model": cfg.get("model", "local-llama"),
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": cfg.get("temperature", 0.7),
        "max_tokens": cfg.get("max_tokens", 512)
    }

    try:
        r = requests.post(llama_url, json=payload)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[DEXOS ERROR] Llama backend issue: {e}"

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])
    print(run_llama(user_input))
