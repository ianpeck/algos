# Given a list of sorted lists, merge them and keep them sorted
def merge(listOfArrays):
    final_list = []
    for list in listOfArrays:
        final_list.extend(list)

    return sorted(final_list)

print(merge([range(500,600),range(1,300),[7,8,9],range(1000,2000)]))