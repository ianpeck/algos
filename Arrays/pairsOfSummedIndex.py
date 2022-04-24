# Given a list of numbers, find all pairs whose index positions add up to the value n.
# For example [1,2,3,4,5,6,7,8,9,10,11], n = 10
# Output would be [ [1,11], [2,10], etc, ...]

def pairsOfSummedIndex(myArray, target):
    pairs = []
    # Loop below only checks half the array because it is a waste to check the other half as it will already be paired in
    for i in range(len(myArray)//2 + 1):
        # Append a list of current value and its indexed pair to our pairs list
        pairs.append([myArray[i], myArray[target - i]])
    
    return pairs



print(pairsOfSummedIndex([1,2,3,4,5,6,7,8,9,10,11], 10))

