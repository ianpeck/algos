def isPalindrome(x):
    x = str(x)
    if x[::-1] == x:
        return True
    else:
        return False
        
# Force the data type to str() then reverse it and see if it is equal to the original!