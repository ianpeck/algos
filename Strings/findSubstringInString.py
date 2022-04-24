# Given a string, find the amount of times a substring occurs in the word

def findSubstring(mystring,mysubstring):
    return mystring.count(mysubstring, 0, len(mystring))

def findSubstringIndices(mystring, mysubstring):
    result = [i for i in range(len(mystring)) if mystring.startswith(mysubstring,i) is True]
    return result




print(findSubstring('mystringystring','string'))
print(findSubstringIndices('mystringystring','string'))