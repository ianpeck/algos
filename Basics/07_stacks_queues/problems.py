"""
STACKS & QUEUES
===============
LIFO (stack) and FIFO (queue) patterns. Stacks especially come up a lot.
In Python: use a list as a stack (append/pop), collections.deque as a queue.

Run this file: python3 problems.py
"""

from collections import deque


# --- Problem 1: Valid parentheses ---
# Given a string of just '(', ')', '{', '}', '[', ']'
# Return True if brackets are properly opened and closed
def valid_parens(s):
    pass


# --- Problem 2: Reverse string with stack ---
# Use a stack (list with append/pop) to reverse a string
def reverse_with_stack(s):
    pass


# --- Problem 3: Min stack ---
# Implement a stack that supports push, pop, and get_min in O(1) time
class MinStack:
    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def get_min(self):
        # Return the minimum value currently in the stack
        pass


# --- Problem 4: Queue using two stacks ---
# Implement a queue (FIFO) using only two stacks (lists with append/pop)
class QueueFromStacks:
    def __init__(self):
        pass

    def enqueue(self, val):
        pass

    def dequeue(self):
        # Return and remove the front element
        pass


# --- Problem 5: Next greater element ---
# For each element, find the next element to its right that is greater
# [4, 2, 6, 1, 3] => [6, 6, -1, 3, -1]
# Use a stack for O(n) solution
def next_greater(nums):
    pass


# --- Problem 6: Evaluate reverse polish notation ---
# ["2", "3", "+", "4", "*"] => (2+3)*4 = 20
# Operators: +, -, *, / (integer division, truncate toward zero)
def eval_rpn(tokens):
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

    print("\n--- Min Stack ---")
    ms = MinStack()
    ms.push(3)
    ms.push(1)
    ms.push(2)
    test("min is 1", ms.get_min(), 1)
    ms.pop()
    test("still 1", ms.get_min(), 1)
    ms.pop()
    test("now 3", ms.get_min(), 3)

    print("\n--- Queue From Stacks ---")
    q = QueueFromStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    test("first out", q.dequeue(), 1)
    test("second out", q.dequeue(), 2)
    q.enqueue(4)
    test("third out", q.dequeue(), 3)
    test("fourth out", q.dequeue(), 4)

    print("\n--- Next Greater ---")
    test("basic", next_greater([4, 2, 6, 1, 3]), [6, 6, -1, 3, -1])
    test("descending", next_greater([5, 4, 3]), [-1, -1, -1])
    test("ascending", next_greater([1, 2, 3]), [2, 3, -1])

    print("\n--- Eval RPN ---")
    test("add mul", eval_rpn(["2", "3", "+", "4", "*"]), 20)
    test("complex", eval_rpn(["4", "13", "5", "/", "+"]), 6)
    test("subtract", eval_rpn(["3", "4", "-"]), -1)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
