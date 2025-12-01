#!/usr/bin/env python3
"""
DexOS Perception Gateway v0.1
Filters world inputs into structured summaries for DexOS.
"""

def gateway_filter(raw_input: str):
    """
    Basic filter to sanitize and format incoming content.
    """
    return f"[GATEWAY] INPUT RECEIVED:\n{raw_input.strip()}\n"

if __name__ == "__main__":
    print(gateway_filter("test input"))
