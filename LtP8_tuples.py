# A tuple is similar to list with the exception that values
# inside a tuple can't change once assigned
myTuple = (1, 2, 3, 5, 8)
# most of the same functions and attributes are similar
# like in lists - indexes
print("1st value: ", myTuple[0])
# tuple slice
print(myTuple[0:3])
# length of a tuple - number of values stored
print("Tuple length: ", len(myTuple))
# join tuples - adding more values
moreFibs = myTuple + (13, 21, 34)
print(moreFibs[5:7])
# check if value is inside a tuple
print("32 in tuple: ", 34 in moreFibs)
# list all values in tuple
for i in moreFibs:
    print(i)
# convert list to tuple
aList = [55, 89, 144]
aTuple = tuple(aList)
# convert back - tuple to list
aList = list(aTuple)
# reading max and min values from tuple
print("Min: ", min(aTuple))
print("Max: ", max(aTuple))
