# SETS — SYNTAX CHEAT SHEET

# Creating sets
s = set()             # empty set  (NOT {} — that's a dict)
s = {1, 2, 3}         # set literal
s = set([1, 2, 2, 3]) # from list, deduplicates automatically

# Modifying sets
s.add(x)              # add single element
s.discard(x)          # remove if present, NO error if missing
s.remove(x)           # remove, errors if not found
s.pop()               # remove and return an arbitrary element

# Membership — O(1)
x in s                # True/False
x not in s            # True/False

# Set operations — operator syntax
a | b                 # union: everything in a OR b
a & b                 # intersection: only in BOTH
a - b                 # difference: in a but NOT in b
a ^ b                 # symmetric difference: in one but NOT both

# Set operations — method syntax (same results)
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)

# Set comparisons
a.issubset(b)         # True if all of a is in b
a.issuperset(b)       # True if a contains all of b
a.isdisjoint(b)       # True if a and b share no elements

# Convert back to sorted list
sorted(s)
