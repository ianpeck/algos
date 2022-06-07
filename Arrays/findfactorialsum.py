def find_factorial(num):
    # if 1 or 0 then return 1
    if num in list([0,1]):
        return 1
    else:
        current_value = 0
        for i in range(1,num):
            if i == 1:
                current_value += i*(i+1)
            else:
                current_value = current_value*(i+1)
        return current_value

def sum_of_facts(num):
    list_of_facts = [find_factorial(i) for i in range(0,num+1)]
    return sum(list_of_facts)


print(sum_of_facts(4))

