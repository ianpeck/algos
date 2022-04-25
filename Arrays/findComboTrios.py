def find_trios(mylist,target):
    combos = []
    used_numbers = []
    for i in range(len(mylist)):
        if mylist[i] not in used_numbers:
            used_numbers.append(mylist[i])
            for x in range((i+1), len(mylist)):
                for y in range((x+1), len(mylist)):
                    if sum([mylist[i],mylist[x],mylist[y]]) == target:
                        if [mylist[i],mylist[x],mylist[y]] not in combos:
                            combos.append([mylist[i],mylist[x],mylist[y]])
    return combos



print(find_trios([1,2,3,4,5,6,7,8,9,10],9))


