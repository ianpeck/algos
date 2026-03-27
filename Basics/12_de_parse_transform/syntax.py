# DE: PARSE, CLEAN & TRANSFORM — SYNTAX CHEAT SHEET

# Safe type coercion
int("42")                   # "42" → 42 (errors on non-numeric)
float("3.14")               # "3.14" → 3.14
str(42)                     # 42 → "42"
try:
    val = int(x)
except (ValueError, TypeError):
    val = None              # handle bad input gracefully

# Null/missing handling
val = row.get("field")          # None if key missing
val = row.get("field") or 0     # None/falsy → 0
val if val is not None else 0   # explicit None check (0 and False stay as-is)

# JSON parsing
import json
data = json.loads('{"key": "val"}')     # string → dict
output = json.dumps(data)               # dict → string
json.dumps(data, indent=2)              # pretty print

# Dict merging / reshaping
{**dict1, **dict2}           # merge (dict2 wins on conflict)
{k: row[k] for k in ["a","b"]}  # select specific keys

# String cleaning
s.strip()                    # remove whitespace
s.strip().lower()            # normalize
s.replace(",", "").strip()   # remove unwanted chars
" ".join(s.split())          # collapse multiple spaces into one

# Flatten nested list one level
[item for sublist in nested for item in sublist]
