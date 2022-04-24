# Given an array, find duplicate values and how many there are, put it into a dictionary

def find_dupes(mylist):
    dupedict = {}
    for value in mylist:
        if value not in dupedict:
            if mylist.count(value) > 1:
                dupedict[value] = mylist.count(value)
    return dupedict


print(find_dupes(['Please','excuse', 'me','I', 'am','am','Please', '5','6','excuse','please', 'Please', '10', 'am', 'am']))