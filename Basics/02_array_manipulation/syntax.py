# ARRAY MANIPULATION — SYNTAX CHEAT SHEET

# Slicing  — nums[start:end:step], end is exclusive
nums[1:4]        # elements at index 1, 2, 3
nums[:3]         # first 3 elements
nums[2:]         # from index 2 to end
nums[::-1]       # reversed copy
nums[::2]        # every other element

# Common list methods
nums.append(x)         # add x to the end
nums.extend([1,2,3])   # add multiple elements to the end
nums.insert(i, x)      # insert x at index i, shifts right
nums.pop()             # remove and return last element
nums.pop(i)            # remove and return element at index i
nums.remove(x)         # remove FIRST occurrence of value x (errors if not found)
nums.index(x)          # return index of first occurrence of x

# Building arrays
[0] * n                    # list of n zeros
list(range(n))             # [0, 1, 2, ..., n-1]
[x for x in nums if x > 0] # list comprehension with filter

# Concatenation and repetition
a + b              # new list combining both
nums * 3           # repeat list 3 times
