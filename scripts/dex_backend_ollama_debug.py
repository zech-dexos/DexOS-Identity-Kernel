#!/usr/bin/env python3
import json
import sys
import requests

from dex_config_loader import load_config
from dex_kernel_unifier import build_kernel_prompt

def run_debug(user_message):
    cfg = load_config()
    url = cfg["ollama_url"]
    model = cfg["model"]

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": build_kernel_prompt(user_message)}
        ]
    }

    print("=== DEBUG MODE: RAW OLLAMA RESPONSE ===")

    try:
        r = requests.post(url, json=payload)
        raw = r.text
        print(raw)
        print("\n=== END RAW ===")

    except Exception as e:
        print(f"[DEBUG ERROR]: {e}")

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:])
    run_debug(msg)
