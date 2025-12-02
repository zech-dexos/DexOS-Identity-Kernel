#!/usr/bin/env python3
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "dex_config.json")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"[CONFIG ERROR] Missing file: {CONFIG_PATH}")
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    print(load_config())
