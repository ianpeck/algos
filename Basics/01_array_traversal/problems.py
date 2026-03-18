"""
ARRAY TRAVERSAL BASICS
======================
The absolute fundamentals. Looping through arrays, accessing elements,
basic operations on each element.

Run this file: python3 problems.py
"""


# --- Problem 1: Sum all elements ---
# Given a list of numbers, return their sum (don't use built-in sum())
def sum_all(nums):
    # accumulator
    running_sum = 0
    for num in nums:
        running_sum += num
    return running_sum



# --- Problem 2: Find the max ---
# Given a list of numbers, return the largest (don't use built-in max())
def find_max(nums):
    running_max = nums[0]  # start with first element as max
    for num in nums:
        if num > running_max:
            running_max = num
    return running_max


# --- Problem 3: Count occurrences ---
# Given a list and a target value, return how many times target appears
def count_occurrences(nums, target):
    running_count = 0
    for num in nums:
        if num == target:
            running_count += 1
    return running_count


# --- Problem 4: Find index ---
# Given a list and a target, return the index of the first occurrence
# Return -1 if not found
def find_index(nums, target):
    for i, val in enumerate(nums): # enumerate gives us both index and value
        if val == target:
            return i # return index immediately when we find it
    return -1


# --- Problem 5: Even numbers only ---
# Given a list of numbers, return a new list with only the even numbers
def evens_only(nums):
    list_of_evens = []
    for num in nums:
        if num % 2 == 0: # if number is divisible by 2, it's even
            list_of_evens.append(num)
    return list_of_evens

# --- Problem 6: Running total ---
# Given [1, 2, 3, 4], return [1, 3, 6, 10]
# Each element is the sum of all elements up to that index
def running_total(nums):
    running_total = 0
    totals = []
    for num in nums:
        running_total += num # add current number to running total
        totals.append(running_total)
    return totals


# --- Problem 7: Reverse iteration ---
# Return elements in reverse order as a list
# Looping backwards cheat sheet:
#   enumerate(nums[::-1])  — reverse values, i is 0,1,2 (not original indices)
#   reversed(nums)         — reverse iterator, no index
#   range(len(nums)-1,-1,-1) — original indices counting down
#   nums[::-1]             — slice, returns new reversed list
def reverse_iterate(nums):
    return nums[::-1]


# --- Problem 8: Pair adjacent ---
# Given [1, 2, 3, 4], return [(1,2), (2,3), (3,4)]
# Return pairs of each element with its neighbor
def pair_adjacent(nums):
    pairs = []
    for i in range(len(nums) - 1): # subtract 1 from range loop that is len of list (up until last value then stop since we use next value in list)
        pairs.append((nums[i],nums[i+1])) # enter a tuple of cur and next value
    return pairs


# --- Problem 9: Middle slice ---
# Given a list and two indices (start, end), return a slice of elements.
# If inclusive is True, include the end index. If False, exclude it.
# Slicing is exclsusive by default, so we can just add 1 to end index if inclusive is True.
# e.g. middle_slice([10, 20, 30, 40, 50], 1, 4) => [20, 30, 40]
# e.g. middle_slice([10, 20, 30, 40, 50], 1, 4, inclusive=True) => [20, 30, 40, 50]
def middle_slice(nums, start, end, inclusive=False):
    if inclusive:
        end += 1 # if we want to include the end index, we need to add 1 to it for slicing
    return nums[start:end] # slice from start to end (exclusive by default, inclusive if we added 1)


# ============ TESTS ============
if __name__ == "__main__":
    passed = 0
    failed = 0

    def test(name, got, expected):
        global passed, failed
        if got == expected:
            print(f"  PASS: {name}")
            passed += 1
        else:
            print(f"  FAIL: {name} — got {got}, expected {expected}")
            failed += 1

    print("--- Sum All ---")
    test("basic", sum_all([1, 2, 3]), 6)
    test("single", sum_all([5]), 5)
    test("negatives", sum_all([-1, -2, 3]), 0)

    print("\n--- Find Max ---")
    test("basic", find_max([1, 5, 3, 9, 2]), 9)
    test("negatives", find_max([-3, -1, -7]), -1)
    test("single", find_max([42]), 42)

    print("\n--- Count Occurrences ---")
    test("multiple", count_occurrences([1, 2, 3, 2, 2], 2), 3)
    test("none", count_occurrences([1, 2, 3], 5), 0)
    test("all same", count_occurrences([7, 7, 7], 7), 3)

    print("\n--- Find Index ---")
    test("found", find_index([10, 20, 30], 20), 1)
    test("first element", find_index([5, 6, 7], 5), 0)
    test("not found", find_index([1, 2, 3], 9), -1)

    print("\n--- Evens Only ---")
    test("mixed", evens_only([1, 2, 3, 4, 5, 6]), [2, 4, 6])
    test("no evens", evens_only([1, 3, 5]), [])
    test("all even", evens_only([2, 4]), [2, 4])

    print("\n--- Running Total ---")
    test("basic", running_total([1, 2, 3, 4]), [1, 3, 6, 10])
    test("single", running_total([5]), [5])
    test("zeros", running_total([0, 0, 0]), [0, 0, 0])

    print("\n--- Reverse Iterate ---")
    test("basic", reverse_iterate([1, 2, 3]), [3, 2, 1])
    test("single", reverse_iterate([9]), [9])

    print("\n--- Pair Adjacent ---")
    test("basic", pair_adjacent([1, 2, 3, 4]), [(1,2), (2,3), (3,4)])
    test("two", pair_adjacent([5, 10]), [(5, 10)])
    test("single", pair_adjacent([1]), [])

    print("\n--- Middle Slice ---")
    test("basic", middle_slice([10, 20, 30, 40, 50], 1, 4), [20, 30, 40])
    test("from start", middle_slice([1, 2, 3, 4], 0, 2), [1, 2])
    test("to end", middle_slice([1, 2, 3, 4], 2, 4), [3, 4])
    test("single element", middle_slice([1, 2, 3], 1, 2), [2])

    print("\n--- Middle Slice (inclusive) ---")
    test("basic incl", middle_slice([10, 20, 30, 40, 50], 1, 4, inclusive=True), [20, 30, 40, 50])
    test("from start incl", middle_slice([1, 2, 3, 4], 0, 2, inclusive=True), [1, 2, 3])
    test("single incl", middle_slice([1, 2, 3], 1, 1, inclusive=True), [2])

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
