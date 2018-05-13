# list comprehension is going to execute an expression
# against an iterable - much as "map" and "filter"
# while a list comprehension is powerful it has to be used
# with cautious to not get overcomplicated

# use different methods to obtain the same list
# of values: multiplication by 2 using map and lc
# a) map
print(list(map((lambda x: x*2), range(1,11))))
# b) list comprehension - it is stored in [] brackets
# and automatically generates a list (therefore no need
# to specify list in expression)
print([2 * x for x in range(1, 11)])

# use different methods to obtain the same list
# of values: only odds using filter and lc
# a) filter - get only odd values
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
# b) list comprehension - use the same expression but
# put it in "if" statement inside "for" loop
print([x for x in range(1, 11) if x % 2 != 0])

# more complicated example - generate 50 values and take
# to the power of 2; then return only multiples of 8
print([i ** 2 for i in range(50) if i % 8 == 0])

# it is also allowed to use multiple "for" loops inside
# list comprehension method - prepare a script that
# generates a list of 2 other lists multiplied by one
# another
print([x*y for x in range(1, 3) for y in range(11, 16)])

# it is possible to put list comprehension inside other
# list comprehension (lc), example: generate a list of 10
# values, multiply them by 2 and return multiples of 8
print([x for x in [i * 2 for i in range(10)]
       if x % 8 == 0])



