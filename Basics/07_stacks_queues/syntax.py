# STACKS & QUEUES — SYNTAX CHEAT SHEET

# Stack — LIFO (last in, first out) — use a plain list
stack = []
stack.append(x)      # push onto top
stack.pop()          # pop from top (errors if empty)
stack[-1]            # peek at top without removing
if stack:            # always check before pop/peek

# Queue — FIFO (first in, first out) — use collections.deque
from collections import deque
q = deque()
q.append(x)          # enqueue to right
q.popleft()          # dequeue from left  ← O(1), unlike list.pop(0) which is O(n)
q.appendleft(x)      # add to front
q[-1]                # peek at back
q[0]                 # peek at front
if q:                # check if non-empty

# Matching brackets pattern (stack classic)
pairs = {")": "(", "]": "[", "}": "{"}
stack = []
for ch in s:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if not stack or stack[-1] != pairs[ch]:
            return False
        stack.pop()
return len(stack) == 0
