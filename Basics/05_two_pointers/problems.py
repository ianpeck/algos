"""
TWO POINTERS
============
The two-pointer technique — left/right pointers moving toward each other,
or a slow/fast read/write pointer pattern.

Run this file: python3 problems.py
"""


# --- Problem 1: Is sorted ---
# Check if array is sorted in ascending order using two adjacent pointers
def is_sorted(nums):
    # left should always be lower than right to be sorted
    left = 0
    right = 1
    while right < len(nums): # while the list still has room to loop
        if nums[left] <= nums[right]: # left number is less than or equal to right number
            left += 1
            right += 1
        else:
            return False
    return True


# --- Problem 2: Reverse array in place ---
# Use left/right pointers to reverse. Modify the list in place, return it.
# [1,2,3,4] => [4,3,2,1]
def reverse_in_place(nums):
    left = 0
    right = len(nums) - 1
    while right > left: # stop once right crosses left to avoid re-reversing
        nums[right], nums[left] = nums[left], nums[right]
        left += 1
        right -= 1
    return nums



# --- Problem 3: Two sum sorted ---
# Given a SORTED array and target, find two numbers that add to target
# Return their indices as a tuple. Use two pointers, not a dict.
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1 # start at last index
    while right > left:
        if nums[left] + nums[right] > target:
            right -= 1 # try a smaller right if sum is greater than target
        elif nums[left] + nums[right] < target:
            left += 1 # try a larger left if sum is less than target
        elif nums[left] + nums[right] == target:
            return (left, right) # if equal return tuple
    return None


# --- Problem 4: Remove duplicates from sorted array ---
# Given sorted array, remove dupes in place and return the new length
# e.g. [1,1,2,2,3] => first 3 elements should be [1,2,3], return 3
# basically we are writing over the dupes from left to right with the unique numbers found by the read, then progressing the write 1 each time it happens. Read always progresse 1.
# write always is the position of the next item to be replaced
def remove_dupes_sorted(nums):
    read = 1
    write = 1

    while read < len(nums): # while there are still numbers to read
        if nums[read] != nums[write - 1]: # if the current read number is different than the last written number, we want to write it
            nums[write] = nums[read]
            write += 1 # move write forward to be ready to write the next unique number
        read += 1 # always move read forward to keep checking numbers until we reach the end of the list

    return write


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

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
