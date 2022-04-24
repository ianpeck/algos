# Given a list and a sum, find all combo pairs of numbers that will add up to it

def find_combos_pairs(mylist, target):
    my_pairs = []
    for i in range(len(mylist)//2):
        if target - mylist[i] in mylist and mylist.index(target - mylist[i]) != i:
            my_pairs.append([mylist[i], target - mylist[i]])
    return my_pairs



 
print(find_combos_pairs([1,2,3,4,5,6,7,8,9,10], 10))