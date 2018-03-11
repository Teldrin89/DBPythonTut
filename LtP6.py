import random
import math

# List and algorithms

# [0: "string"] [1 : 1.234] [2 : 28]
# Lists in python can grow in size and contain different type of data

randList = ["string", 1.234, 28]
# You can create a list with a range
oneToTen = list(range(10))

# On lists there is a way to use most of the same functions as on
# strings (like for example slice)
# Concatenate (combine)
randList = randList + oneToTen
# Get the first item
print(randList[0])
# Get length of the list
print("List length: ", len(randList))
# Slice the list
first3 = randList[0:3]
# Print out the index and data related to that index
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Print out list item multiple times
print(first3[0] * 3)
# Check if an item is inside a list
print("string" in first3)
# Check the index of a specific string
print("Index of a string: ", first3.index("string"))
# How many items an item is inside a list
print("How many strings: ", first3.count("string"))
# Change list item
first3[0] = "New string"
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Appending a list item (put another at the end of a list)
first3.append("Another")
for i in first3:
    print("{} : {}".format(first3.index(i), i))




