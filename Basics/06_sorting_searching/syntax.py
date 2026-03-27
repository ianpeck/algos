# SORTING & SEARCHING — SYNTAX CHEAT SHEET

# Sorting
sorted(nums)                        # returns new sorted list (ascending)
sorted(nums, reverse=True)          # descending
sorted(words, key=len)              # sort by string length
sorted(pairs, key=lambda x: x[1])  # sort list of tuples by second element
nums.sort()                         # sort in place (no return value)
nums.sort(key=lambda x: -x)        # in-place descending

# Binary search template — O(log n), requires SORTED input
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2       # integer division
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1              # target is in right half
    else:
        right = mid - 1             # target is in left half
return -1                           # not found

# bisect module — binary search built-in
import bisect
bisect.bisect_left(nums, x)         # index to insert x keeping sorted order (left of dupes)
bisect.bisect_right(nums, x)        # same but right of dupes
