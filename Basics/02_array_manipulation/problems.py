"""
ARRAY MANIPULATION
==================
Modifying arrays — in-place changes, building new arrays, slicing.

Run this file: python3 problems.py
"""


# --- Problem 1: Swap first and last ---
# Modify the list in place so first and last elements are swapped
# Return the list
def swap_first_last(nums):
    pass


# --- Problem 2: Remove all occurrences ---
# Return a new list with all occurrences of target removed
def remove_all(nums, target):
    pass


# --- Problem 3: Rotate left by k ---
# [1,2,3,4,5] rotated left by 2 => [3,4,5,1,2]
def rotate_left(nums, k):
    pass


# --- Problem 4: Interleave two arrays ---
# Given [1,2,3] and [a,b,c], return [1,a,2,b,3,c]
# If one is longer, append the remaining elements
def interleave(a, b):
    pass


# --- Problem 5: Flatten nested list (one level) ---
# [[1,2], [3,4], [5]] => [1,2,3,4,5]
# Only one level deep — don't worry about deeply nested
def flatten(nested):
    pass


# --- Problem 6: Chunk array ---
# Split array into chunks of size n
# [1,2,3,4,5] with n=2 => [[1,2], [3,4], [5]]
def chunk(nums, n):
    pass


# --- Problem 7: Move zeros to end ---
# [0, 1, 0, 3, 12] => [1, 3, 12, 0, 0]
# Maintain relative order of non-zero elements
def move_zeros(nums):
    pass


# --- Problem 8: Deduplicate (keep order) ---
# [1, 3, 2, 3, 1, 4] => [1, 3, 2, 4]
# Remove duplicates but keep the first occurrence in original order
def deduplicate(nums):
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

    print("--- Swap First Last ---")
    test("basic", swap_first_last([1, 2, 3, 4]), [4, 2, 3, 1])
    test("two", swap_first_last([1, 2]), [2, 1])
    test("single", swap_first_last([1]), [1])

    print("\n--- Remove All ---")
    test("basic", remove_all([1, 2, 3, 2, 4], 2), [1, 3, 4])
    test("none found", remove_all([1, 2, 3], 5), [1, 2, 3])
    test("all removed", remove_all([7, 7, 7], 7), [])

    print("\n--- Rotate Left ---")
    test("by 2", rotate_left([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
    test("by 1", rotate_left([1, 2, 3], 1), [2, 3, 1])
    test("full rotation", rotate_left([1, 2, 3], 3), [1, 2, 3])

    print("\n--- Interleave ---")
    test("equal", interleave([1, 2, 3], ['a', 'b', 'c']), [1, 'a', 2, 'b', 3, 'c'])
    test("a longer", interleave([1, 2, 3], ['a']), [1, 'a', 2, 3])
    test("b longer", interleave([1], ['a', 'b', 'c']), [1, 'a', 'b', 'c'])

    print("\n--- Flatten ---")
    test("basic", flatten([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])
    test("empty inner", flatten([[], [1], []]), [1])
    test("single", flatten([[1]]), [1])

    print("\n--- Chunk ---")
    test("even", chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
    test("remainder", chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
    test("size 1", chunk([1, 2, 3], 1), [[1], [2], [3]])

    print("\n--- Move Zeros ---")
    test("basic", move_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
    test("no zeros", move_zeros([1, 2, 3]), [1, 2, 3])
    test("all zeros", move_zeros([0, 0, 0]), [0, 0, 0])

    print("\n--- Deduplicate ---")
    test("basic", deduplicate([1, 3, 2, 3, 1, 4]), [1, 3, 2, 4])
    test("no dupes", deduplicate([1, 2, 3]), [1, 2, 3])
    test("all same", deduplicate([5, 5, 5]), [5])

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
