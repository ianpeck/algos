# Using two for loops, loop throught the original list, checking to see if our current number is smaller than
# the previous number. If it is, we loop through the sorted list up to that index to see where our current 
# number fits in it and then we swap their positions once we find the point where our number is less than the
# indexed number in the sorted portion of the list.

list_1 = [1,17,5]

def bin_sort(my_list):
    # for every value in the length of the list
    for i in range(len(my_list)):
        # if the current value is less than the previous value
        if my_list[i] < my_list[i-1]:
            # loop through all the previous values in the list, up to the index of our current number
            for j in range(i):
                # find the point where the current number fits in the sorted array
                if my_list[i] < my_list[j]:
                    # swap their positiions in the list
                    my_list[i], my_list[j] = my_list[j], my_list[i]

    
    return my_list

print(bin_sort(list_1))
