# Problem20: find the multiples of 9 from a random 100 value
# list with values between 1 and 1000
# DB solution using the filter function and less code

# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values

# import random module
import random

# create a random list with numbers in range 1 to 1000
# and with 100 elements
rand_list = list(random.randint(1, 1001) for i in range(100))

# use modulus to find multiples of 9
# printout the new list of numbers generated using the
# filter function with inside function using lambda -
# that is checking for only modulus of 9 - in random list
# generated line before
print(list(filter((lambda x: x % 9 == 0), rand_list)))
