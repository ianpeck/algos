# Given a list, find the frequency of each value in it

AList = ['string', 'string', 'ape', 'fling', 'ape', 'monk', 'Ian', '4', 'ape', 'monk', 'celery', 'tidal', 'string']

def findFrequency(mylist):
    hashmap = {}
    for x in mylist:
        if x not in hashmap:
            hashmap[x] = mylist.count(x)
    return hashmap

print(findFrequency(AList))

    
