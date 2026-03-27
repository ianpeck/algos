# DE: STREAMING & SLIDING WINDOW — SYNTAX CHEAT SHEET

# Fixed-size sliding window — track sum/avg over last N elements
from collections import deque
window = deque()
window_sum = 0
for x in stream:
    window.append(x)
    window_sum += x
    if len(window) > N:
        window_sum -= window.popleft()   # drop oldest
    avg = window_sum / len(window)

# Variable window — expand right, shrink left when condition breaks
left = 0
for right in range(len(nums)):
    # include nums[right] in window
    while <window violates condition>:
        # remove nums[left] from window
        left += 1
    # window nums[left:right+1] is valid here

# Running state in single pass
running_sum = 0
running_max = float('-inf')
running_min = float('inf')
for x in stream:
    running_sum += x
    running_max = max(running_max, x)
    running_min = min(running_min, x)

# Emit results one at a time (generator pattern)
def process(stream):
    state = {}
    for event in stream:
        # update state
        yield result    # yield instead of append to avoid holding all in memory
