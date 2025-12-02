#!/usr/bin/env python3
"""
DexOS Perception Gateway v0.3
Simple filter → wraps external input into a tagged block.
"""

def gateway_filter(raw_input: str) -> str:
    return f"[GATEWAY FILTERED INPUT]\n{raw_input.strip()}\n[END INPUT]\n"

if __name__ == "__main__":
    print(gateway_filter("test input"))
