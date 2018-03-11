import random
import math

# list generated similar as to in problem 11
num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 10))

# sorting list
num_list.sort()
# reverse sorting
num_list.reverse()
# change value at specific index  -in this example it inserts
# number "10" at index 5
num_list.insert(5, 10)
# remove item from list
num_list.remove(10)
# remove item at specific index
num_list.pop(2)

for k in num_list:
    print(k, end=", ")
print()

# list comprehensions - a way to create a list by doing operations
# on each item in a list

# this will generate list of 10 items, each multiplied by 2
even_list = [i*2 for i in range(10)]
# printout the resulting list
for i in even_list:
    print(i)

# Create a list of lists with the same method (using multiple
# different calculations)

# List of 5 items
numberList = [1,2,3,4,5]
# List of 5 lists with 3 items in each (to the power of 2,3 and 4)
listOfValues = [[math.pow(m, 2), math.pow(m,3), math.pow(m, 4)]
                for m in numberList]
# printout results
for i in listOfValues:
    print(i)
print()

# create 10x10 list of lists - this one is populated by "0"
multiDlist = [[0] * 10 for i in range(10)]

for i in multiDlist:
    print(i)
print()

# change values in the list
multiDlist[0][1] = 10

for i in multiDlist:
    print(i)
print()

# Specific indexes for 2D matrix (list of lists)
# Establish "empty" (filled with "0") list of lists - 4x4
listTable = [[0]*4 for i in range(4)]
# for loops going through 2 dimensions of matrix (call them "x"
# and "y") and store the indexes in each value separated by "|"
for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i, j)
# printout the results - each value and each row in new line
for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" | ")
    print()
# printout full list of lists
print(listTable)
