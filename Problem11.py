# Problem11: Generate a random list (random values in a list)
# 5 values between 1 and 9; for this it will be needed a random
# generation, for loop and list creation

import math
import random

# My approach at the problem solution: no need for math import
# First, the empty list is established, then there is for loop
# running for 5 items, each time appending the number in a list
rand_list = []
for i in range(1, 5):
    rand_number = random.randrange(1, 10)
    rand_list.append(rand_number)
print(rand_list)

# Mostly the same as in DB (with one line less as you can append
# without having the random number variable
