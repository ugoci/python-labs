# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

from re import U


example_list = [1, 2, 3, 4, 5, 6, 7]


def stat1(l):
    largest_num = max(l)
    return largest_num

def stat2(u):
    the_sum = sum(u)
    return the_sum

def stat3(u):
    lenth = len(u)
    return lenth     

def stat4(n):
    average = stat2(n) / stat3(n)
    return average

print(stat1(example_list))
print(stat2(example_list))
print(stat3(example_list))
print(stat4(example_list))

