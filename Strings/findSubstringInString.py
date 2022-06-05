# Given a string, find the amount of times a substring occurs in the word

def findSubstring(mystring,mysubstring):
    # Iterates through a slice of string (whole thing in this case) and counts how many times the substring occurs
    return mystring.count(mysubstring, 0, len(mystring))


def findSubstringIndices(mystring, mysubstring):
    # Iterates the length of the string, checking if the string starts with our substring at each index
    result = []
    for i in range(len(mystring)):
        if mystring.startswith(mysubstring, i):
            result.append(i)
    return result
    # Alternative way to do the first function (findSubstring) is to just return the lenth of this variable below.
    return len(result)




print(findSubstring('mystringystring','string'))
print(findSubstringIndices('mystringystring','string'))