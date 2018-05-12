# iterable - it is a stored sequence of values (or put it
# simply it is a list of values); it also can act as an
# object that produce a single value at a time
# iterator - it is an object with a method "__next__" -
# that retrieves next value form a sequence of values

# create a sample string value
strSample = iter("Sample")
# printout the next character from string
print("Char: ", next(strSample))
# using the same command 2nd time is returning the next
# character from sample string
print("Char: ", next(strSample))
