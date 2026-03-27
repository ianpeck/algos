# ARRAY TRAVERSAL — SYNTAX CHEAT SHEET

# List comprehension
[x for x in nums]                    # basic
[x for x in nums if x > 0]          # with filter
[x * 2 for x in nums if x % 2 == 0] # transform + filter

# enumerate — get index AND value
for i, val in enumerate(nums):       # i=0,1,2...  val=element

# range patterns
range(len(nums))                     # 0 to n-1
range(1, len(nums))                  # 1 to n-1 (skip first)
range(len(nums) - 1, -1, -1)        # countdown from last index to 0
range(0, len(nums), 2)              # every other index

# zip — loop two lists together
for a, b in zip(list1, list2):       # stops at shorter list
for a, b in zip(list1, list2[1:]):   # pair each element with next (sliding window of 2)

# reverse iteration
nums[::-1]                           # new reversed list
reversed(nums)                       # iterator, no index
