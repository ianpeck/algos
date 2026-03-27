# DE: GROUP BY + AGGREGATE & JOINS — SYNTAX CHEAT SHEET

# Group by pattern — build {key: [values]} from a list of records
groups = {}
for row in rows:
    key = row["dept"]
    groups.setdefault(key, []).append(row)  # setdefault init + append in one line

# Or with defaultdict
from collections import defaultdict
groups = defaultdict(list)
for row in rows:
    groups[row["dept"]].append(row)

# Aggregate after grouping
{k: sum(v) for k, v in groups.items()}        # sum per group
{k: len(v) for k, v in groups.items()}        # count per group
{k: max(v) for k, v in groups.items()}        # max per group
{k: sum(v) / len(v) for k, v in groups.items()}  # average per group

# Inner join on key — keep only rows with a match in both
lookup = {row["id"]: row for row in table2}    # build lookup dict from right table
result = []
for row in table1:
    if row["id"] in lookup:
        result.append({**row, **lookup[row["id"]]})  # merge both dicts

# Left join — keep all rows from left, fill None if no match
for row in table1:
    match = lookup.get(row["id"])              # None if not found
    result.append({**row, **(match or {})})
