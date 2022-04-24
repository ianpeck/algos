# Concept: Hash Table 

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    duotable = {}
    for i, num in enumerate(nums): 
        if num in duotable:
            # Return list of indexes of compliment and number if it exists in the hash table
            return [duotable[num], i]
        else:
            # Add compliment of your num and index of your num to hash table (dictionary) to future referencing
            # target-num (your duo) is the key of your duotable dictionary, its index (i) is the value
            duotable[target-num] = i

print(twoSum([1,3,3,5,6,7,8,9,10,11,4,5,2,4,5,6],3))

# Expected Output = [0, 12]

# Solution: Use a hashtable, or a table that stores previous iterations and indexes of those numbers. 
# The idea is that you loop through your numbers list from start and store the duo that would add up to the target 
# and the index of the original num
# When the duo finally appears when looping through your numbers list, your return the index of the duo and index of your current num


        