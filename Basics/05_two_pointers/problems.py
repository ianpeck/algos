"""
TWO POINTERS
============
The two-pointer technique — left/right pointers moving toward each other,
or a slow/fast pointer pattern. Super common in interviews.

Run this file: python3 problems.py
"""


# --- Problem 1: Is sorted ---
# Check if array is sorted in ascending order using two adjacent pointers
def is_sorted(nums):
    pass


# --- Problem 2: Reverse array in place ---
# Use left/right pointers to reverse. Modify the list in place, return it.
def reverse_in_place(nums):
    pass


# --- Problem 3: Two sum sorted ---
# Given a SORTED array and target, find two numbers that add to target
# Return their indices as a tuple. Use two pointers, not a dict.
def two_sum_sorted(nums, target):
    pass


# --- Problem 4: Remove duplicates from sorted array ---
# Given sorted array, remove dupes in place and return the new length
# e.g. [1,1,2,2,3] => first 3 elements should be [1,2,3], return 3
def remove_dupes_sorted(nums):
    pass


# --- Problem 5: Container with most water (simplified) ---
# Given array of heights, find two lines that form a container holding the most water
# Water = min(height[l], height[r]) * (r - l)
# Return the max water amount
def max_water(heights):
    pass


# --- Problem 6: Valid palindrome with cleanup ---
# Check if string is palindrome considering only alphanumeric chars, case insensitive
# "A man, a plan, a canal: Panama" => True
def is_valid_palindrome(s):
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

    print("--- Is Sorted ---")
    test("yes", is_sorted([1, 2, 3, 4]), True)
    test("no", is_sorted([1, 3, 2, 4]), False)
    test("empty", is_sorted([]), True)
    test("single", is_sorted([5]), True)

    print("\n--- Reverse In Place ---")
    test("basic", reverse_in_place([1, 2, 3, 4]), [4, 3, 2, 1])
    test("single", reverse_in_place([1]), [1])

    print("\n--- Two Sum Sorted ---")
    test("basic", two_sum_sorted([1, 2, 3, 4, 5], 9), (3, 4))
    test("first two", two_sum_sorted([1, 3, 5, 7], 4), (0, 1))

    print("\n--- Remove Dupes Sorted ---")
    arr1 = [1, 1, 2, 2, 3]
    n1 = remove_dupes_sorted(arr1)
    test("length", n1, 3)
    test("values", arr1[:n1], [1, 2, 3])

    arr2 = [1, 1, 1]
    n2 = remove_dupes_sorted(arr2)
    test("all same", n2, 1)

    print("\n--- Max Water ---")
    test("basic", max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    test("simple", max_water([1, 1]), 1)

    print("\n--- Valid Palindrome ---")
    test("with punctuation", is_valid_palindrome("A man, a plan, a canal: Panama"), True)
    test("not palindrome", is_valid_palindrome("race a car"), False)
    test("empty", is_valid_palindrome(""), True)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
