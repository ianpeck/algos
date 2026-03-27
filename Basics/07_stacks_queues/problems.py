"""
STACKS & QUEUES
===============
In Python: use a list as a stack (append/pop), collections.deque as a queue.
Kept to the two problems most likely to appear in a DE interview.

Run this file: python3 problems.py
"""


# --- Problem 1: Valid parentheses ---
# Given a string of just '(', ')', '{', '}', '[', ']'
# Return True if brackets are properly opened and closed
def valid_parens(s):
    pass


# --- Problem 2: Reverse string with stack ---
# Use a stack (list with append/pop) to reverse a string
def reverse_with_stack(s):
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

    print("--- Valid Parens ---")
    test("simple", valid_parens("()"), True)
    test("mixed", valid_parens("()[]{}"), True)
    test("nested", valid_parens("{[()]}"), True)
    test("invalid", valid_parens("(]"), False)
    test("unclosed", valid_parens("(("), False)

    print("\n--- Reverse With Stack ---")
    test("basic", reverse_with_stack("hello"), "olleh")
    test("single", reverse_with_stack("a"), "a")

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
