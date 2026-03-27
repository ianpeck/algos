# DE: DEDUPLICATION & LATEST STATE — SYNTAX CHEAT SHEET

# Simple dedup — preserve first occurrence, maintain order
seen = set()
result = []
for row in rows:
    key = row["id"]
    if key not in seen:
        seen.add(key)
        result.append(row)

# Keep LAST occurrence (latest state per key)
latest = {}
for row in rows:
    latest[row["id"]] = row          # later rows overwrite earlier ones
result = list(latest.values())

# Keep row with MAX value per key (e.g. latest timestamp)
latest = {}
for row in rows:
    key = row["id"]
    if key not in latest or row["ts"] > latest[key]["ts"]:
        latest[key] = row

# Dedup within sorted data — compare to previous
prev = None
for row in sorted_rows:
    if row["id"] != prev:
        result.append(row)
    prev = row["id"]
