# DICT / HASHMAP BASICS — SYNTAX CHEAT SHEET

# Looping through dicts — 3 ways
for k in d:                    # keys only (same as d.keys())
for v in d.values():           # values only
for k, v in d.items():         # key-value pairs — most common

# Safe access
d.get("key")                   # returns None if missing (no KeyError)
d.get("key", 0)                # returns 0 if missing
d.setdefault("key", [])        # insert default if key missing, then return it

# Dict comprehension
{k: v for k, v in pairs}                      # basic
{k: v * 2 for k, v in d.items()}              # transform values
{k: v for k, v in d.items() if v > 0}         # filter
{v: k for k, v in d.items()}                  # invert keys/values

# Nested dicts
d = {"a": {"x": 1, "y": 2}}
d["a"]["x"]                    # access nested value 1
d.setdefault("b", {})["z"] = 3 # safely add to nested

# defaultdict — never need to initialize a key
from collections import defaultdict
d = defaultdict(int)           # missing key → 0
d = defaultdict(list)          # missing key → []
d = defaultdict(set)           # missing key → set()
