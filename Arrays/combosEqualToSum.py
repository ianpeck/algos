# Given a list and a sum, find all combo pairs of numbers that will add up to it

def find_combos_pairs(mylist, target):
    my_pairs = []
    hashmap = {}
    for i in range(len(mylist)//2):
        # if the target pair is in the list, the number is not the same index (the same 5 and 5 cannot add to 10), and the pair is not already in there
        if target - mylist[i] in mylist and mylist.index(target - mylist[i]) != i and i not in hashmap: 
            my_pairs.append([mylist[i], target - mylist[i]])
            hashmap[mylist.index(target - mylist[i])] = target - mylist[i]
    return my_pairs



 
print(find_combos_pairs([1,2,3,4,5,6,7,8,9,10], 7))