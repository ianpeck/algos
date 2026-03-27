"""
SORTING & SEARCHING
====================
Skip implementing basic sorts — Python's sorted() handles that.
Focus on binary search (log n lookup) and merge patterns.

Run this file: python3 problems.py
"""


# --- Problem 1: Binary search ---
# Given a SORTED list and target, return the index of target
# Return -1 if not found. Must be O(log n).
def binary_search(nums, target):
    pass


# --- Problem 2: Find insert position ---
# Given a sorted list and target, return the index where target should be inserted
# to keep the list sorted. If target exists, return its index.
def search_insert(nums, target):
    pass


# --- Problem 3: Merge two sorted arrays ---
# Given two sorted arrays, merge them into one sorted array
def merge_sorted(a, b):
    pass


# --- Problem 4: Kth smallest element ---
# Find the kth smallest element in an unsorted array (1-indexed)
# k=1 means the smallest
def kth_smallest(nums, k):
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

    print("--- Binary Search ---")
    test("found", binary_search([1, 3, 5, 7, 9], 5), 2)
    test("first", binary_search([1, 3, 5, 7, 9], 1), 0)
    test("last", binary_search([1, 3, 5, 7, 9], 9), 4)
    test("not found", binary_search([1, 3, 5, 7, 9], 4), -1)

    print("\n--- Search Insert ---")
    test("exists", search_insert([1, 3, 5, 7], 5), 2)
    test("insert middle", search_insert([1, 3, 5, 7], 4), 2)
    test("insert start", search_insert([1, 3, 5], 0), 0)
    test("insert end", search_insert([1, 3, 5], 6), 3)

    print("\n--- Merge Sorted ---")
    test("basic", merge_sorted([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
    test("one empty", merge_sorted([], [1, 2]), [1, 2])
    test("overlap", merge_sorted([1, 2], [2, 3]), [1, 2, 2, 3])

    print("\n--- Kth Smallest ---")
    test("1st", kth_smallest([5, 3, 1, 4, 2], 1), 1)
    test("3rd", kth_smallest([5, 3, 1, 4, 2], 3), 3)
    test("last", kth_smallest([5, 3, 1, 4, 2], 5), 5)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
