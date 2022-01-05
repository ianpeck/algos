# Write a function that returns the smallest key (sorted in ascending order alphabetically) of the given input dictionary containing nth highest value

#  For example:
# - dictionary : {"a":1, "b": 2, "c": 100, "d": 30, "f":30}
# - n : 2 (2nd highest value)
# - output : "d"
def findvalue(n, dict):
    # create unique list of numbers out of dictionary values, utilizing built-in Python "set" DS to filter out duplicate numbers
    my_unique_list = list(set(dict.values()))
    # sort that unqiue list in ascending order (can also use sorted())
    # sorted(my_unique_list,reverse=False))
    my_unique_list.sort()
    # set a variable equal to the nth highest value in your list, if 2 is entered in, the 2nd to last number in the list will be returned, or the 2nd largest number
    my_num = my_unique_list[-n]
    # return the first instance of that number's key, utilizng two lists, one of the dictionary's keys, one of its values.
    # finding the index of your number and using it to find it's matching key
    return list(dict.keys())[list(dict.values()).index(my_num)]

# Additional way (iterates though, is slower)
def findvalue2(n,dict):
    my_unique_list = list(set(dict.values()))
    my_unique_list.sort()
    my_num = my_unique_list[-n]
    for key, value in list(dict.items()):
        if value == my_num:
            return key


    
print(findvalue(3, {"a":1, "b": 2, "c": 100, "d": 30, "f":30}))
print(findvalue2(3, {"a":1, "b": 2, "c": 100, "d": 30, "f":30}))