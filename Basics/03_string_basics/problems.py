"""
STRING BASICS
=============
Iterating strings, character operations, building strings.

Run this file: python3 problems.py
"""


# --- Problem 1: Count vowels ---
# Return the number of vowels (a, e, i, o, u) in a string (case insensitive)
def count_vowels(s):
    count = 0
    for letter in s:
        if letter in 'aeiouAEIOU':
            count += 1
    return count


# --- Problem 2: Reverse a string ---
def reverse_string(s):
    return s[::-1] # slice with step of -1 to reverse string


# --- Problem 3: Is palindrome ---
# Check if a string reads the same forwards and backwards (case insensitive)
# Ignore spaces
def is_palindrome(s):
    string = s.lower().replace(" ","")
    if string == string[::-1]:
        return True
    else:
        return False

# --- Problem 4: Character frequency ---
# Return a dict of {char: count} for each character in the string
# e.g. "aab" => {'a': 2, 'b': 1}
def char_frequency(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1 # add 1 to existing count
        else:
            char_dict[char] = 1 # initialize count to 1 for new character
    return char_dict


# --- Problem 5: First non-repeating character ---
# Return the first character that appears only once
# Return None if all repeat
def first_unique_char(s):
    char_counter= {}
    for char in s:
        if char in char_counter:
            char_counter[char] += 1 # add 1 to existing count
        else:
            char_counter[char] = 1 # initialize count to 1 for new character
    for char in s:
        if char_counter[char] == 1: # check if count is 1 for current character in original string order
            return char
    return None



# --- Problem 6: Compress string ---
# "aaabbc" => "a3b2c1"
# If compressed is not shorter, return the original string
def compress(s):
    final_string = ""
    char_dict = char_frequency(s) # use char counter function
    for key, value in char_dict.items(): # loop through the dict of letters and counts and concat them to empty string
        final_string += (key + str(value))
    return final_string


# --- Problem 7: Are anagrams ---
# Check if two strings are anagrams of each other (case insensitive, ignore spaces)
def are_anagrams(s1, s2):
    def clean_string(s):
        return s.replace(" ","").lower()
    return sorted(clean_string(s1)) == sorted(clean_string(s2)) # sort the strings after clean and set them equal


# --- Problem 8: Title case ---
# "hello world foo" => "Hello World Foo"
# Don't use .title() — do it manually
def title_case(s):
    final_string = ""
    word_list = s.split(" ")
    for word in word_list:
        final_string += word[0].upper() + word[1::] + " "
    return final_string.strip()

        




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

    print("--- Count Vowels ---")
    test("basic", count_vowels("hello"), 2)
    test("uppercase", count_vowels("AEIOU"), 5)
    test("none", count_vowels("xyz"), 0)

    print("\n--- Reverse String ---")
    test("basic", reverse_string("hello"), "olleh")
    test("single", reverse_string("a"), "a")
    test("empty", reverse_string(""), "")

    print("\n--- Is Palindrome ---")
    test("yes", is_palindrome("racecar"), True)
    test("no", is_palindrome("hello"), False)
    test("mixed case", is_palindrome("Aba"), True)
    test("with spaces", is_palindrome("taco cat"), True)

    print("\n--- Character Frequency ---")
    test("basic", char_frequency("aab"), {'a': 2, 'b': 1})
    test("single", char_frequency("x"), {'x': 1})

    print("\n--- First Unique Char ---")
    test("basic", first_unique_char("aabbc"), 'c')
    test("first", first_unique_char("abcabc"), None)
    test("middle", first_unique_char("aabcbd"), 'c')

    print("\n--- Compress ---")
    test("compresses", compress("aaabbc"), "a3b2c1")
    test("no benefit", compress("abc"), "abc")
    test("single char", compress("aaa"), "a3")

    print("\n--- Are Anagrams ---")
    test("yes", are_anagrams("listen", "silent"), True)
    test("no", are_anagrams("hello", "world"), False)
    test("case insensitive", are_anagrams("Tea", "Eat"), True)

    print("\n--- Title Case ---")
    test("basic", title_case("hello world"), "Hello World")
    test("single", title_case("foo"), "Foo")
    test("already", title_case("Hello"), "Hello")

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed+failed}")
