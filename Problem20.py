# Problem20: find the multiples of 9 from a random 100 value
# list with values between 1 and 1000
import random
# Generate a random list using "randint" between 1 and 1000
# and put them in single list - "rand_list"
# Use modulus to find multiples of 9 and put the result
# in next list - "div_9"
# do all in single for loop
rand_list = []
div_9 = []
for i in range(100):
    rand_list.append(random.randint(1, 1000))
    if rand_list[i-1]%9 == 0:
        div_9.append(rand_list[i-1])

# printout the list of randomly generated integers
print(rand_list)
# printout the resulting list of integers divided by 9
# plus number of values
print(div_9, "Number of elements divided by 9:", len(div_9))
