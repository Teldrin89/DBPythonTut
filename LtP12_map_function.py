# the map function allows to execute a function on
# every item in a list

# create a list
oneTo10 = range(1, 11)


# create a function that will be passed in map
# function and will return a double value
def dbl_number(num):
    return num * 2


# printout the results of multiplication by 2 for whole
# list created using the new function and map function
# use list option to create a new list using the map function
print(list(map(dbl_number, oneTo10)))
# there is also a possibility to pass a function directly
# inside map - use lambda to pass function into the map
# map function - this time to multiply values by 3
print(list(map((lambda x: x * 3), oneTo10)))
# there is a possibility to perform map calculation against
# multiple lists - add values from 1st and 2nd lists
mlist = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(mlist)

# reduce - a function that can receive a list and return
# a single result - this function has t be imported
from functools import reduce
# generate a single number that is the result of single
# function - in this case simple addition of values from
# the provided range
print(reduce((lambda x, y: x + y), range(1, 6)))
