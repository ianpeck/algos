"""
COLLECTIONS & HEAPQ
====================
Python's power tools: Counter for frequency, defaultdict for grouping,
deque for fast queues, heapq for priority/top-K problems.

Run this file: python3 problems.py
"""

from collections import Counter, defaultdict
import heapq


# --- Problem 1: Top K frequent elements ---
# Given a list of numbers, return the k most frequent elements
# Order within the result doesn't matter
# [1, 1, 1, 2, 2, 3], k=2 => [1, 2]
def top_k_frequent(nums, k):
    counts = Counter(nums)
    return [val for val, _ in counts.most_common(k)]


# --- Problem 2: Anagram groups ---
# Given a list of strings, group anagrams together
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# => [["eat","tea","ate"], ["tan","nat"], ["bat"]]  (order within groups doesn't matter)
def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))   # anagrams share the same sorted letters
        groups[key].append(word)
    return list(groups.values())


# --- Problem 3: K closest numbers ---
# Given a sorted list and a target, find the k closest numbers to target
# Return them sorted. If tie in distance, prefer the smaller number.
# nums=[1,2,3,4,5], target=3, k=2 => [2,3]
def k_closest(nums, target, k):
    # push (distance, value) onto heap; ties broken by smaller value (smaller value = smaller distance from target, so it's fine)
    heap = []
    for num in nums:
        dist = abs(num - target)
        heapq.heappush(heap, (dist, num))
    return sorted(val for _, val in heapq.nsmallest(k, heap))


# --- Problem 4: Running median ---
# Process a stream of numbers and after each number report the current median
# [2, 1, 5, 7, 2, 0, 5] => [2, 1.5, 2, 3.5, 2, 2.0, 2]
# Use a max-heap for lower half and min-heap for upper half
def running_median(nums):
    lo = []   # max-heap (negate values): stores lower half
    hi = []   # min-heap: stores upper half
    result = []

    for num in nums:
        # push to lo first, then rebalance
        heapq.heappush(lo, -num)
        # move lo's max to hi if it's larger than hi's min
        heapq.heappush(hi, -heapq.heappop(lo))
        # keep lo same size or one larger than hi
        if len(hi) > len(lo):
            heapq.heappush(lo, -heapq.heappop(hi))

        if len(lo) == len(hi):
            result.append((-lo[0] + hi[0]) / 2)
        else:
            result.append(float(-lo[0]))

    return result


# --- Problem 5: Word frequency top N ---
# Given a string of text, return the N most common words (case insensitive)
# as a list of (word, count) tuples, sorted by count descending
# "the cat sat on the mat the cat", n=2 => [("the", 3), ("cat", 2)]
def top_n_words(text, n):
    words = text.lower().split()
    return Counter(words).most_common(n)


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

    print("--- Top K Frequent ---")
    test("basic", sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])
    test("k=1", sorted(top_k_frequent([4, 4, 4, 3, 3], 1)), [4])
    test("all unique", sorted(top_k_frequent([1, 2, 3], 3)), [1, 2, 3])

    print("\n--- Group Anagrams ---")
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # sort each group and sort the groups to make comparison order-independent
    normalized = sorted([sorted(g) for g in result])
    test("basic", normalized, [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    test("single", group_anagrams(["abc"]), [["abc"]])

    print("\n--- K Closest ---")
    test("basic", k_closest([1, 2, 3, 4, 5], 3, 2), [2, 3])
    test("at edge", k_closest([1, 2, 3, 4, 5], 1, 2), [1, 2])
    test("tie prefers smaller", k_closest([1, 2, 3, 4, 5], 3, 4), [1, 2, 3, 4])

    print("\n--- Running Median ---")
    test("basic", running_median([2, 1, 5, 7, 2, 0, 5]), [2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0])
    test("single", running_median([5]), [5.0])
    test("two", running_median([3, 1]), [3.0, 2.0])

    print("\n--- Top N Words ---")
    test("basic", top_n_words("the cat sat on the mat the cat", 2), [("the", 3), ("cat", 2)])
    test("n=1", top_n_words("a a b b b", 1), [("b", 3)])

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
