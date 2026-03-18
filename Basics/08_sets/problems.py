"""
SETS
====
Uniqueness, membership checks, set operations.
Sets are O(1) lookup — great for "have I seen this?" problems.

Run this file: python3 problems.py
"""


# --- Problem 1: Has duplicates ---
# Return True if any element appears more than once
def has_duplicates(nums):
    pass


# --- Problem 2: Unique elements ---
# Return a list of elements that appear exactly once, in original order
def unique_elements(nums):
    pass


# --- Problem 3: Set difference ---
# Return elements in a that are NOT in b, in original order, no dupes
def difference(a, b):
    pass


# --- Problem 4: Symmetric difference ---
# Return elements in either a or b but NOT in both, sorted
def symmetric_difference(a, b):
    pass


# --- Problem 5: Longest consecutive sequence ---
# Given unsorted array, find the length of the longest consecutive sequence
# [100, 4, 200, 1, 3, 2] => 4 (the sequence 1,2,3,4)
# Must be O(n) — use a set
def longest_consecutive(nums):
    pass


# --- Problem 6: Find missing number ---
# Given array containing n distinct numbers from 0 to n, find the missing one
# [3, 0, 1] => 2 (numbers 0-3, missing 2)
def find_missing(nums):
    pass


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

    print("--- Has Duplicates ---")
    test("yes", has_duplicates([1, 2, 3, 1]), True)
    test("no", has_duplicates([1, 2, 3, 4]), False)
    test("empty", has_duplicates([]), False)

    print("\n--- Unique Elements ---")
    test("basic", unique_elements([1, 2, 3, 2, 1, 4]), [3, 4])
    test("all unique", unique_elements([1, 2, 3]), [1, 2, 3])
    test("none unique", unique_elements([1, 1, 2, 2]), [])

    print("\n--- Difference ---")
    test("basic", difference([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2])
    test("no overlap", difference([1, 2], [3, 4]), [1, 2])
    test("all overlap", difference([1, 2], [1, 2, 3]), [])

    print("\n--- Symmetric Difference ---")
    test("basic", symmetric_difference([1, 2, 3], [2, 3, 4]), [1, 4])
    test("no overlap", symmetric_difference([1, 2], [3, 4]), [1, 2, 3, 4])

    print("\n--- Longest Consecutive ---")
    test("basic", longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
    test("single", longest_consecutive([1]), 1)
    test("empty", longest_consecutive([]), 0)
    test("with dupes", longest_consecutive([1, 2, 2, 3]), 3)

    print("\n--- Find Missing ---")
    test("middle", find_missing([3, 0, 1]), 2)
    test("last", find_missing([0, 1, 2]), 3)
    test("first", find_missing([1, 2, 3]), 0)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
