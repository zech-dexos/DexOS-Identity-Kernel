#!/usr/bin/env python3
"""
DexOS Redirector v0.1
Automatically routes prompts to the correct backend:
- local llama.cpp server
- GPT API
- Claude API
- Grok API
"""

import os
import json
import requests

CONFIG_PATH = os.path.expanduser("config/dex_config.json")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("DexOS config file missing.")
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def call_local_llama(prompt, config):
    try:
        payload = {
            "prompt": prompt,
            "n_predict": config.get("max_tokens", 256),
            "temperature": config.get("temperature", 0.7)
        }
        r = requests.post("http://localhost:8080/completion", json=payload)
        return r.json().get("content", "")
    except:
        return "[DexOS] Local llama.cpp unreachable."

def call_gpt(prompt, config):
    header = {"Authorization": f"Bearer {config.get('api_key')}"}
    body = {
        "model": config.get("model", "gpt-4.1-mini"),
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": config.get("max_tokens", 300)
    }
    r = requests.post("https://api.openai.com/v1/chat/completions", headers=header, json=body)
    return r.json()["choices"][0]["message"]["content"]

def route(prompt):
    config = load_config()
    backend = config.get("backend", "local_llama")

    if backend == "local_llama":
        return call_local_llama(prompt, config)
    elif backend == "gpt":
        return call_gpt(prompt, config)
    else:
        return "[DexOS] Unknown backend."
