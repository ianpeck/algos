"""
DE: GROUP BY + AGGREGATE & JOINS
=================================
Core DE patterns: summarizing datasets and combining two datasets on a key.

Run this file: python3 problems.py
"""


# --- Problem 1: Count events per user ---
# Given a list of event dicts with a "user_id" key,
# return a dict of {user_id: count}
# [{"user_id": 1}, {"user_id": 2}, {"user_id": 1}] => {1: 2, 2: 1}
def count_per_user(events):
    pass


# --- Problem 2: Sum totals by category ---
# Given a list of records with "category" and "amount",
# return {category: total_amount}
# [{"category": "food", "amount": 10}, {"category": "food", "amount": 5}] => {"food": 15}
def sum_by_category(records):
    pass


# --- Problem 3: Average transaction value per account ---
# Given a list of transactions with "account_id" and "amount",
# return {account_id: average_amount} rounded to 2 decimal places
def avg_per_account(transactions):
    pass


# --- Problem 4: Hash join two datasets ---
# Join users and orders on user_id
# users = [{"user_id": 1, "name": "Alice"}, ...]
# orders = [{"user_id": 1, "item": "book"}, ...]
# Return a list of merged dicts for each order:
# [{"user_id": 1, "name": "Alice", "item": "book"}, ...]
# Orders with no matching user are skipped
def hash_join(users, orders):
    pass


# --- Problem 5: Left join (keep all left records) ---
# Same as above but keep all orders even if no matching user
# Fill missing user fields with None
# [{"user_id": 99, "item": "pen"}] => [{"user_id": 99, "name": None, "item": "pen"}]
def left_join(users, orders):
    pass


# --- Problem 6: Top K users by event count ---
# Given a list of events with "user_id", return the top k user_ids by count
# Return as a list sorted descending by count
# If tie, either order is fine
def top_k_users(events, k):
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

    print("--- Count Per User ---")
    test("basic", count_per_user([{"user_id": 1}, {"user_id": 2}, {"user_id": 1}]), {1: 2, 2: 1})
    test("single", count_per_user([{"user_id": 5}]), {5: 1})

    print("\n--- Sum By Category ---")
    test("basic", sum_by_category([
        {"category": "food", "amount": 10},
        {"category": "food", "amount": 5},
        {"category": "travel", "amount": 20}
    ]), {"food": 15, "travel": 20})

    print("\n--- Avg Per Account ---")
    test("basic", avg_per_account([
        {"account_id": "A", "amount": 10},
        {"account_id": "A", "amount": 20},
        {"account_id": "B", "amount": 5}
    ]), {"A": 15.0, "B": 5.0})

    print("\n--- Hash Join ---")
    users = [{"user_id": 1, "name": "Alice"}, {"user_id": 2, "name": "Bob"}]
    orders = [{"user_id": 1, "item": "book"}, {"user_id": 1, "item": "pen"}, {"user_id": 99, "item": "cup"}]
    test("basic", hash_join(users, orders), [
        {"user_id": 1, "name": "Alice", "item": "book"},
        {"user_id": 1, "name": "Alice", "item": "pen"}
    ])

    print("\n--- Left Join ---")
    test("basic", left_join(users, orders), [
        {"user_id": 1, "name": "Alice", "item": "book"},
        {"user_id": 1, "name": "Alice", "item": "pen"},
        {"user_id": 99, "name": None, "item": "cup"}
    ])

    print("\n--- Top K Users ---")
    events = [{"user_id": 1}, {"user_id": 2}, {"user_id": 1}, {"user_id": 3}, {"user_id": 1}, {"user_id": 2}]
    test("top 2", top_k_users(events, 2), [1, 2])
    test("top 1", top_k_users(events, 1), [1])

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
