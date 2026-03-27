# STRING BASICS — SYNTAX CHEAT SHEET

# Strings behave like read-only lists — same slicing rules
s[::-1]          # reversed string
s[1:4]           # substring from index 1 to 3

# Common string methods
s.lower()                  # all lowercase
s.upper()                  # all uppercase
s.strip()                  # remove leading/trailing whitespace
s.lstrip() / s.rstrip()    # strip only left or right side
s.split(" ")               # split on space → list of words
s.split(",")               # split on comma
"sep".join(["a","b","c"])  # "a sep b sep c"  — join list into string
s.replace("old", "new")    # replace all occurrences
s.startswith("abc")        # True/False
s.endswith("xyz")          # True/False
s.count("x")               # count occurrences of substring
s.find("x")                # index of first occurrence, -1 if not found
s.isdigit()                # True if all characters are digits
s.isalpha()                # True if all characters are letters

# Building strings — use list then join (faster than +=)
chars = []
chars.append("a")
result = "".join(chars)    # join with no separator

# f-strings
name = "world"
f"hello {name}"            # "hello world"
f"{num:.2f}"               # float with 2 decimal places

# Checking membership
"e" in "hello"             # True
"x" in "aeiou"             # membership check in a string works like a set
