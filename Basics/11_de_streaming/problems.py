"""
DE: STREAMING & SLIDING WINDOW
================================
Single-pass processing and moving windows — core to pipeline and event stream work.

Run this file: python3 problems.py
"""


# --- Problem 1: Running total ---
# Given a list of numbers, return a list of cumulative sums
# [1, 2, 3, 4] => [1, 3, 6, 10]
def running_total(nums):
    pass


# --- Problem 2: Filter large dataset in one pass ---
# Given a list of records and a condition function, return only matching records
# without building intermediate lists (use a generator)
# Example: filter_stream(records, lambda r: r["amount"] > 100)
def filter_stream(records, condition):
    pass


# --- Problem 3: Sliding window — fixed count ---
# Given a list of numbers and window size k,
# return a list of averages for each window of size k
# [1, 2, 3, 4, 5], k=3 => [2.0, 3.0, 4.0]
def sliding_window_avg(nums, k):
    pass


# --- Problem 4: Sliding window — events in last N minutes ---
# Given a list of events with "ts" (int timestamp in minutes) and a window size,
# and a query timestamp t, return all events where t - window < ts <= t
def events_in_window(events, t, window):
    pass


# --- Problem 5: Streaming max (one pass) ---
# Process a stream of numbers one at a time, track the running maximum
# Return a list of the max seen so far after each element
# [3, 1, 4, 1, 5] => [3, 3, 4, 4, 5]
def running_max(nums):
    pass


# --- Problem 6: Process large file line by line ---
# Given a file path, read it line by line (no loading full file into memory)
# and return a list of lines that contain the keyword (case insensitive)
# This is the memory-efficient file processing pattern
def grep_file(filepath, keyword):
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

    print("--- Running Total ---")
    test("basic", running_total([1, 2, 3, 4]), [1, 3, 6, 10])
    test("single", running_total([5]), [5])

    print("\n--- Filter Stream ---")
    records = [{"amount": 50}, {"amount": 150}, {"amount": 200}, {"amount": 80}]
    test("basic", list(filter_stream(records, lambda r: r["amount"] > 100)),
         [{"amount": 150}, {"amount": 200}])

    print("\n--- Sliding Window Avg ---")
    test("basic", sliding_window_avg([1, 2, 3, 4, 5], 3), [2.0, 3.0, 4.0])
    test("k=1", sliding_window_avg([1, 2, 3], 1), [1.0, 2.0, 3.0])

    print("\n--- Events In Window ---")
    events = [{"ts": 1}, {"ts": 3}, {"ts": 5}, {"ts": 8}, {"ts": 10}]
    test("basic", events_in_window(events, t=8, window=5), [{"ts": 3}, {"ts": 5}, {"ts": 8}])

    print("\n--- Running Max ---")
    test("basic", running_max([3, 1, 4, 1, 5]), [3, 3, 4, 4, 5])
    test("descending", running_max([5, 4, 3]), [5, 5, 5])

    print("\n--- Grep File ---")
    # Create a temp test file
    import tempfile, os
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Hello World\nerror: something failed\nall good\nERROR again\n")
        tmp = f.name
    test("case insensitive", grep_file(tmp, "error"),
         ["error: something failed\n", "ERROR again\n"])
    os.unlink(tmp)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
