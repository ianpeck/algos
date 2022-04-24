# Check if any combo of the word can be rewritten the same front as backwards
# The key here is to know a palindrome cannot have more than one character that has an odd count as that would not allow it to mirror on both sides of the letter

def is_palindrome(s):
    odd_counter = 0
    for letter in s:
        if s.count(letter) % 2 != 0:
            odd_counter += 1
        if odd_counter > 1:
            return False
    return True

print(is_palindrome('rqarayraaryj'))