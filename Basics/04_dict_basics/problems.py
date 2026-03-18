"""
DICT / HASHMAP BASICS
=====================
Counting, grouping, lookups — the bread and butter of data engineering interviews.

Run this file: python3 problems.py
"""


# --- Problem 1: Word count ---
# Given a list of words, return a dict of {word: count}
def word_count(words):
    pass


# --- Problem 2: Two sum (return indices) ---
# Given nums and a target, return indices of two numbers that add to target
# Return as a tuple (i, j) where i < j. Assume exactly one solution exists.
def two_sum(nums, target):
    pass


# --- Problem 3: Group by length ---
# Given a list of strings, group them by their length
# {"cat": 3, "hi": 2, "dog": 3, "me": 2} => {3: ["cat", "dog"], 2: ["hi", "me"]}
def group_by_length(words):
    pass


# --- Problem 4: Invert a dict ---
# {a: 1, b: 2} => {1: a, 2: b}
# Assume values are unique
def invert_dict(d):
    pass


# --- Problem 5: Merge two dicts (sum values) ---
# {a: 1, b: 2} + {b: 3, c: 4} => {a: 1, b: 5, c: 4}
def merge_sum(d1, d2):
    pass


# --- Problem 6: Most frequent element ---
# Return the element that appears most often in a list
# If tie, return any of them
def most_frequent(nums):
    pass


# --- Problem 7: Are all values unique ---
# Check if all values in a list are unique
def all_unique(nums):
    pass


# --- Problem 8: Find intersection ---
# Return elements that appear in both lists (no duplicates in result)
# Preserve order from first list
def intersection(a, b):
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

    print("--- Word Count ---")
    test("basic", word_count(["a", "b", "a", "c", "b", "a"]), {"a": 3, "b": 2, "c": 1})
    test("single", word_count(["x"]), {"x": 1})

    print("\n--- Two Sum ---")
    test("basic", two_sum([2, 7, 11, 15], 9), (0, 1))
    test("later", two_sum([3, 2, 4], 6), (1, 2))

    print("\n--- Group By Length ---")
    test("basic", group_by_length(["cat", "hi", "dog", "me"]), {3: ["cat", "dog"], 2: ["hi", "me"]})
    test("single", group_by_length(["a"]), {1: ["a"]})

    print("\n--- Invert Dict ---")
    test("basic", invert_dict({"a": 1, "b": 2}), {1: "a", 2: "b"})

    print("\n--- Merge Sum ---")
    test("overlap", merge_sum({"a": 1, "b": 2}, {"b": 3, "c": 4}), {"a": 1, "b": 5, "c": 4})
    test("no overlap", merge_sum({"a": 1}, {"b": 2}), {"a": 1, "b": 2})

    print("\n--- Most Frequent ---")
    test("basic", most_frequent([1, 2, 2, 3, 3, 3]), 3)
    test("single", most_frequent([5]), 5)

    print("\n--- All Unique ---")
    test("yes", all_unique([1, 2, 3, 4]), True)
    test("no", all_unique([1, 2, 3, 1]), False)

    print("\n--- Intersection ---")
    test("basic", intersection([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
    test("none", intersection([1, 2], [3, 4]), [])
    test("dupes", intersection([1, 1, 2], [1, 1]), [1])

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
