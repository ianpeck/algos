"""
DE: PARSE, CLEAN & TRANSFORM
==============================
Handling messy real-world data: nulls, nested structures, type coercion, reshaping.

Run this file: python3 problems.py
"""

import json


# --- Problem 1: Parse JSON string safely ---
# Given a string that may or may not be valid JSON,
# return the parsed object or None if invalid
def parse_json_safe(s):
    pass


# --- Problem 2: Flatten nested dict (one level) ---
# {"user": {"id": 1, "name": "Alice"}, "score": 99}
# => {"user_id": 1, "user_name": "Alice", "score": 99}
# Use underscore to join parent and child keys
def flatten_dict(d, prefix=""):
    pass


# --- Problem 3: Fill missing fields with defaults ---
# Given a list of records and a defaults dict,
# return records with any missing keys filled in from defaults
# records = [{"id": 1, "name": "Alice"}, {"id": 2}]
# defaults = {"name": "unknown", "active": True}
# => [{"id": 1, "name": "Alice", "active": True}, {"id": 2, "name": "unknown", "active": True}]
def fill_defaults(records, defaults):
    pass


# --- Problem 4: Drop records with null required fields ---
# Given a list of records and required field names,
# return only records where all required fields are non-None and non-empty-string
def drop_nulls(records, required_fields):
    pass


# --- Problem 5: Remap field names ---
# Given a list of records and a mapping {old_name: new_name},
# return records with fields renamed. Unknown fields are kept as-is.
# records = [{"uid": 1, "amt": 50}], mapping = {"uid": "user_id", "amt": "amount"}
# => [{"user_id": 1, "amount": 50}]
def remap_fields(records, mapping):
    pass


# --- Problem 6: Flatten list of nested event records ---
# Each record has a "user_id" and a list of "events"
# Return one row per event with user_id attached
# [{"user_id": 1, "events": ["click", "view"]}]
# => [{"user_id": 1, "event": "click"}, {"user_id": 1, "event": "view"}]
def explode_events(records):
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

    print("--- Parse JSON Safe ---")
    test("valid", parse_json_safe('{"a": 1}'), {"a": 1})
    test("invalid", parse_json_safe("not json"), None)
    test("empty", parse_json_safe(""), None)

    print("\n--- Flatten Dict ---")
    test("nested", flatten_dict({"user": {"id": 1, "name": "Alice"}, "score": 99}),
         {"user_id": 1, "user_name": "Alice", "score": 99})
    test("flat", flatten_dict({"a": 1, "b": 2}), {"a": 1, "b": 2})

    print("\n--- Fill Defaults ---")
    test("basic", fill_defaults(
        [{"id": 1, "name": "Alice"}, {"id": 2}],
        {"name": "unknown", "active": True}
    ), [{"id": 1, "name": "Alice", "active": True}, {"id": 2, "name": "unknown", "active": True}])

    print("\n--- Drop Nulls ---")
    test("basic", drop_nulls([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": None},
        {"id": 3, "name": ""}
    ], ["id", "name"]), [{"id": 1, "name": "Alice"}])

    print("\n--- Remap Fields ---")
    test("basic", remap_fields(
        [{"uid": 1, "amt": 50}, {"uid": 2, "amt": 75}],
        {"uid": "user_id", "amt": "amount"}
    ), [{"user_id": 1, "amount": 50}, {"user_id": 2, "amount": 75}])

    print("\n--- Explode Events ---")
    test("basic", explode_events([
        {"user_id": 1, "events": ["click", "view"]},
        {"user_id": 2, "events": ["purchase"]}
    ]), [
        {"user_id": 1, "event": "click"},
        {"user_id": 1, "event": "view"},
        {"user_id": 2, "event": "purchase"}
    ])

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
