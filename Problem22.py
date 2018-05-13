# Problem22 - generate a list of 50 random values between
# 1 and 1000 and return those that are multiples of 9
# try to use the lc inside of another lc
# import random module to generate random numbers
import random

# printout only values that are dividable by 9 (modulus
# equal to 0), out of the 50 random values (between 1 and
#  1000 values generated using for loop inside the lc
print([x for x in [random.randrange(1, 1001) for i in
                   range(50)] if x % 9 == 0])
# done myself :) looks exactly the same as DB
