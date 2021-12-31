# Find integer length of longest substring in string wihout a repeating character.

def lengthOfLongestSubstring(string):
    used = {}
    max_length = start = 0
    for i, letter in enumerate(string):

        if letter in used and start <= used[letter]:
            start = used[letter] + 1

        else:
            max_length = max(max_length, i - start + 1)
            
        used[letter] = i

    return max_length

print(lengthOfLongestSubstring('abcdbd'))