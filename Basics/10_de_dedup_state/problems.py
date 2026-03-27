"""
DE: DEDUPLICATION & LATEST STATE
==================================
Dedup variants and tracking the most recent value per entity —
common in ETL pipelines and event stream processing.

Run this file: python3 problems.py
"""


# --- Problem 1: Dedup keep first occurrence ---
# Given a list of dicts with an "id" field, remove duplicates keeping the first seen
# [{"id": 1, "val": "a"}, {"id": 1, "val": "b"}] => [{"id": 1, "val": "a"}]
def dedup_keep_first(records):
    pass


# --- Problem 2: Dedup keep last occurrence ---
# Same but keep the last seen record for each id
# [{"id": 1, "val": "a"}, {"id": 1, "val": "b"}] => [{"id": 1, "val": "b"}]
def dedup_keep_last(records):
    pass


# --- Problem 3: Dedup keep latest by timestamp ---
# Each record has "id" and "timestamp" (int, higher = newer)
# Return one record per id: the one with the highest timestamp
# [{"id": 1, "ts": 100, "val": "old"}, {"id": 1, "ts": 200, "val": "new"}]
# => [{"id": 1, "ts": 200, "val": "new"}]
def dedup_by_timestamp(records):
    pass


# --- Problem 4: Maintain latest state per key ---
# Given a stream of status events [{"user_id": X, "status": Y, "ts": Z}],
# return a dict of {user_id: status} showing the most recent status per user
# {"user_id": 1: "active", "user_id": 2: "inactive"}
def latest_status(events):
    pass


# --- Problem 5: Find records changed between two snapshots ---
# Given old_records and new_records (lists of dicts with "id"),
# return a dict with:
#   "added":   ids in new but not in old
#   "removed": ids in old but not in new
#   "same":    ids in both
def diff_snapshots(old_records, new_records):
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

    print("--- Dedup Keep First ---")
    test("basic", dedup_keep_first([
        {"id": 1, "val": "a"}, {"id": 2, "val": "b"}, {"id": 1, "val": "c"}
    ]), [{"id": 1, "val": "a"}, {"id": 2, "val": "b"}])

    print("\n--- Dedup Keep Last ---")
    test("basic", dedup_keep_last([
        {"id": 1, "val": "a"}, {"id": 2, "val": "b"}, {"id": 1, "val": "c"}
    ]), [{"id": 2, "val": "b"}, {"id": 1, "val": "c"}])

    print("\n--- Dedup By Timestamp ---")
    test("basic", dedup_by_timestamp([
        {"id": 1, "ts": 100, "val": "old"},
        {"id": 1, "ts": 200, "val": "new"},
        {"id": 2, "ts": 50, "val": "only"}
    ]), [{"id": 1, "ts": 200, "val": "new"}, {"id": 2, "ts": 50, "val": "only"}])

    print("\n--- Latest Status ---")
    test("basic", latest_status([
        {"user_id": 1, "status": "active", "ts": 100},
        {"user_id": 2, "status": "inactive", "ts": 50},
        {"user_id": 1, "status": "churned", "ts": 200}
    ]), {1: "churned", 2: "inactive"})

    print("\n--- Diff Snapshots ---")
    old = [{"id": 1}, {"id": 2}, {"id": 3}]
    new = [{"id": 2}, {"id": 3}, {"id": 4}]
    test("basic", diff_snapshots(old, new), {"added": {4}, "removed": {1}, "same": {2, 3}})

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
