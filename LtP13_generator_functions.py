# generator function will generate individual values one
# at a time (rather then all at once)
# main use for generators is when user handles a large
# number of results and to avoid throttling the system
# user works on part of the data, iteratively called and
# stored results


# create a function that will check if number is a prime
# number
def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    # returns True for every other case (will include 2
    # - number from which it starts), if "True" would be
    # kept in "if" statement it would not include the "2"
    return True


# create a function that will generate,iteratively next
# prime numbers
def gen_primes(max_number):
    # run a for loop from 2 to provided max number
    for num1 in range(2, max_number):
        # use "isprime" function to check if a value is
        # prime number
        if isprime(num1):
            # if true, get that value
            yield num1


# assign the next prime values to "prime" variable
prime = gen_primes(50)
# printout the results of next prime numbers using "next"
# method (iterative)
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))

# generator expressions look exactly as the list
# comprehensions except the fact that they return
# values one at a time instead of all at once

# the syntax difference between ge and lc is the type of
# bracket (parenthesis instead of square)
double = (x * 2 for x in range(10))
# get 2 first values
print("Double: ", next(double))
print("Double: ", next(double))
# for loop to get all values - start from next as there
# have been 2 read before
for num in double:
    print(num)
