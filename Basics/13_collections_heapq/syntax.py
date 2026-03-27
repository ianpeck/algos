# COLLECTIONS & HEAPQ — SYNTAX CHEAT SHEET

# Counter — frequency map in one line
from collections import Counter
c = Counter(["a", "b", "a", "c", "a"])  # Counter({'a': 3, 'b': 1, 'c': 1})
c["a"]                   # 3
c.most_common(2)         # [('a', 3), ('b', 1)] — top 2 by count
c.most_common()[-1]      # least common
Counter("hello")         # works on strings too: {'l':2,'h':1,'e':1,'o':1}
dict(c)                  # convert back to plain dict

# defaultdict — auto-initialize missing keys
from collections import defaultdict
d = defaultdict(int)     # missing key → 0
d = defaultdict(list)    # missing key → []
d = defaultdict(set)     # missing key → set()
d["x"] += 1              # no KeyError, starts at 0
d["y"].append(5)         # no KeyError, starts as []

# deque — O(1) appends/pops from both ends
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)             # add right
dq.appendleft(0)         # add left
dq.pop()                 # remove right
dq.popleft()             # remove left — O(1), unlike list.pop(0)
dq.maxlen                # optional max size (set in constructor)

# heapq — min-heap (smallest element always at index 0)
import heapq
heap = []
heapq.heappush(heap, 5)  # push element
heapq.heappush(heap, 2)
heapq.heappop(heap)      # pop and return smallest (2 here)
heap[0]                  # peek at smallest without removing

heapq.heapify(nums)      # convert list to heap IN PLACE — O(n)
heapq.nlargest(3, nums)  # top 3 largest — O(n log k)
heapq.nsmallest(3, nums) # top 3 smallest

# Max-heap trick — negate values (Python only has min-heap)
heapq.heappush(heap, -val)   # push negated
-heapq.heappop(heap)         # pop and negate back

# Push tuples to sort by priority, then break ties with second element
heapq.heappush(heap, (priority, value))
