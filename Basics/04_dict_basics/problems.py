"""
DICT / HASHMAP BASICS
=====================
Counting, grouping, lookups — the bread and butter of data engineering interviews.

Run this file: python3 problems.py
"""


# --- Problem 1: Word count ---
# Given a list of words, return a dict of {word: count}
# can use cnt_dict.get(word, 0) + 1 as well
# .get() will grab the value of that key, else default to something
def word_count(words):
    cnt_dict = {}
    for word in words:
        if word not in cnt_dict:
            cnt_dict[word] = 0
        if word in cnt_dict:
            cnt_dict[word] += 1
    return cnt_dict


# --- Problem 2: Two sum (return indices) ---
# Unsorted array, return indices of two numbers that add to target
# Given nums and a target, return indices of two numbers that add to target
# Return as a tuple (i, j) where i < j. Assume exactly one solution exists.
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return (seen[difference],i)
        else:
            seen[num] = i




# --- Problem 3: Group by length ---
# Given a list of strings, group them by their length
# ["cat", "hi", "dog", "me"] => {3: ["cat", "dog"], 2: ["hi", "me"]}
def group_by_length(words):
    final_dict = {}
    for word in words:
        length_of_word = len(word)
        if length_of_word not in final_dict: # could also use defaultdict(list)
            final_dict[length_of_word] = []
        final_dict[length_of_word].append(word)
    return final_dict




# --- Problem 4: Invert a dict ---
# {a: 1, b: 2} => {1: a, 2: b}
# Assume values are unique
def invert_dict(d):
    new_dict = {}
    for k, v in d.items():
        new_dict[v] = k
    return new_dict



# --- Problem 5: Merge two dicts (sum values) ---
# {a: 1, b: 2} + {b: 3, c: 4} => {a: 1, b: 5, c: 4}
def merge_sum(d1, d2):
    final_dict = d1.copy()
    for k, v in d2.items():
        if k not in final_dict:
            final_dict[k] = v
        else:
            final_dict[k] += v
    return final_dict




from collections import defaultdict
# --- Problem 6: Most frequent element ---
# Return the element that appears most often in a list
# If tie, return any of them
# if no default dict, then use dict.get(key, 0)
def most_frequent(nums):
    seen = defaultdict(int)
    largest_count = 0
    largest_count_num = 0
    for num in nums:
        seen[num] += 1
        if seen[num] > largest_count:
            largest_count = seen[num]
            largest_count_num = num
    return largest_count_num

# --- Problem 7: Are all values unique ---
# Given a list, return True if no element appears more than once, False otherwise
def all_unique(nums):
    nums_set = set(nums)
    if len(nums_set) == len(nums):
        return True
    else:
        return False


# --- Problem 8: Find intersection ---
# Given two lists, return only the elements that exist in BOTH
# No duplicates in result, keep the order from the first list
# [1, 2, 2, 3] and [2, 3, 4] => [2, 3]
def intersection(a, b):
    # must preserve a so we need to loop through that normally
    # remove dupes with sets
    set_b = set(b)
    seen = set()
    result = []
    for num in a:
        # we want to append to list if number is in b_set (intersect) and has not yet been seen in our loop
        if num not in seen and num in set_b:
            seen.add(num)
            result.append(num)
    return result



# --- Problem 9: Dict comprehension — filter and transform ---
# Given a dict of {name: score}, return a new dict with only scores >= 70,
# but multiply each passing score by 1.1 (round to 2 decimal places)
# must use dict comprehension
# {"alice": 80, "bob": 60, "carol": 90} => {"alice": 88.0, "carol": 99.0}
def passing_scores(scores):
    return {name: round(score * 1.1, 2) for name, score in scores.items() if score >= 70}


# --- Problem 10: Nested dict — group and count ---
# Given a list of (department, employee) tuples, build a nested dict:
# {department: {"employees": [names], "count": n}}
# [("eng", "alice"), ("eng", "bob"), ("hr", "carol")]
# => {"eng": {"employees": ["alice", "bob"], "count": 2}, "hr": {"employees": ["carol"], "count": 1}}
def group_by_dept(records):
    result = {}
    for dept, name in records:
        if dept not in result:
            result[dept] = {"employees": [], "count": 0}
        result[dept]["employees"].append(name)
        result[dept]["count"] += 1
    return result


# --- Problem 11: Aggregate stats from list of dicts ---
# Given a list of records like [{"id": "a", "value": 10}, {"id": "a", "value": 20}, ...]
# return a dict of {id: {"sum": ..., "count": ..., "avg": ...}}
# avg should be rounded to 2 decimal places
# [{"id": "a", "value": 10}, {"id": "b", "value": 5}, {"id": "a", "value": 30}]
# => {"a": {"sum": 40, "count": 2, "avg": 20.0}, "b": {"sum": 5, "count": 1, "avg": 5.0}}
def aggregate_stats(records):
    final_dict = {}
    for row in records:
        id = row["id"] # set vars early as to not be confusing
        val = row["value"]
        if id not in final_dict: # insert a blank default dict in if id not in final dict
            final_dict[id] = {"sum": 0, "count": 0, 'avg': 0}
        final_dict[id]['sum'] += val
        final_dict[id]['count'] += 1
        final_dict[id]['avg'] = round(final_dict[id]['sum'] / final_dict[id]['count'], 1) # round to 1 decimal
    return final_dict




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

    print("\n--- Passing Scores ---")
    test("basic", passing_scores({"alice": 80, "bob": 60, "carol": 90}), {"alice": 88.0, "carol": 99.0})
    test("none pass", passing_scores({"x": 50, "y": 60}), {})
    test("all pass", passing_scores({"a": 70, "b": 100}), {"a": 77.0, "b": 110.0})

    print("\n--- Group By Dept ---")
    test("basic", group_by_dept([("eng", "alice"), ("eng", "bob"), ("hr", "carol")]),
         {"eng": {"employees": ["alice", "bob"], "count": 2}, "hr": {"employees": ["carol"], "count": 1}})
    test("single", group_by_dept([("eng", "alice")]),
         {"eng": {"employees": ["alice"], "count": 1}})

    print("\n--- Aggregate Stats ---")
    test("basic", aggregate_stats([{"id": "a", "value": 10}, {"id": "b", "value": 5}, {"id": "a", "value": 30}]),
         {"a": {"sum": 40, "count": 2, "avg": 20.0}, "b": {"sum": 5, "count": 1, "avg": 5.0}})
    test("single", aggregate_stats([{"id": "x", "value": 7}]),
         {"x": {"sum": 7, "count": 1, "avg": 7.0}})
    test("three ids", aggregate_stats([{"id": "a", "value": 1}, {"id": "b", "value": 2}, {"id": "c", "value": 3}]),
         {"a": {"sum": 1, "count": 1, "avg": 1.0}, "b": {"sum": 2, "count": 1, "avg": 2.0}, "c": {"sum": 3, "count": 1, "avg": 3.0}})

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
