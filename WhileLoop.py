import random

# Imported one of the libraries to help with while loop example

rand_num = random.randrange(1, 51)

i = 1

# The while loop is looping as long as you have a true statement
while i != rand_num:
    i += 1

print("The random value is: ", rand_num)

# Break and continue in while loop

i = 1

# We are going to continue wo cycle through values as long as i
# is less then or equal to 20
while i <= 20:
    if i % 2 == 0:
        i += 1
        # The continue function will ignore everything below in
        # while loop and get back to the beginning of this while
        continue

    if i == 15:
        break
# The break function will completely force the code
# to get outside of the while loop
    print("Odd : ", i)
    i += 1


