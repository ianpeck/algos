# Given an array of numbers, find the missing number.

def findMissingNumber(mylist):
    n = len(mylist)
    # Formula for finding sum of 1 to n numbers
    total = (n + 1)*(n + 2)/2
    sum_of_mylist = sum(mylist)
    # Subtract
    return total - sum_of_mylist

print(findMissingNumber([1,2,3,4,6]))