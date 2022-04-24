# Given an array and a window size, find duplicate values and how many there are, put it into a dictionary

def find_dupes(mylist,k):
    dupedict = {}
    mySlicedList = mylist[0:k]
    for value in mySlicedList:
        if value not in dupedict:
            if mySlicedList.count(value) > 1:
                dupedict[value] = mySlicedList.count(value)
    return dupedict


print(find_dupes(['Please','excuse', 'me','I', 'am','am','Please', '5','6','excuse','please', 'Please', '10', 'am', 'am'],6))


