# TWO POINTERS — SYNTAX CHEAT SHEET

# Converging pointers — start at both ends, move inward
left, right = 0, len(nums) - 1
while left < right:
    # do something with nums[left] and nums[right]
    left += 1    # or right -= 1 depending on logic

# Sliding window — two pointers both moving right
left = 0
for right in range(len(nums)):
    # expand window by advancing right
    while <window too big>:
        left += 1   # shrink from left

# Read/write pointers — overwrite in place
read, write = 1, 1
while read < len(nums):
    if <keep this element>:
        nums[write] = nums[read]
        write += 1
    read += 1
# write is the new length after compaction

# Common swap pattern (no temp variable needed)
nums[left], nums[right] = nums[right], nums[left]
