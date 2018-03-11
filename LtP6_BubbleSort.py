import random
import math

# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of
#   the list when outer loop completes 1 cycle - this way
#   the next time the cycle goes through the list it goes through
#   less number of indexes in list as largest is already set
# 3. The inner loop starts comparing indexes at the beginning
#   of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at
#   the end of the list
# 7. Decrement the outer loop by 1

# Use the randomly generated list of numbers from previous problem
num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 10))
# Create a value to be decrementing in outer loop
# This is going to be the length of list -1 (as we have
# indexes starting from 0)
i = len(num_list) - 1
# The outer loop to be cycling through the list until we get
# to first index - [0]
while i > 1:
    j = 0
    # The inner loop
    while j < i:
        # The large number of print statements is purely for
        # debugging of the code
        # Printing out 1st and 2nd index and if one is grater than
        # the other
        print("\nIs {} > {}".format(num_list[j], num_list[j + 1]))
        if num_list[j] > num_list[j+1]:
            # If the condition is met we swap variables
            # using a temporary variable
            print("Switch")
            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j+1] = temp
        else:
            print("Don't switch")
        # Increment the value of j - going from left to right
        j += 1
        # Printing out each time the whole list to track changes
        for k in num_list:
            print(k, end=", ")
        print()
    # Decrement value of i - going from right to left
    # Print out the hint that one cycle of sorting has ended
    print("End of round")
    i -= 1
# Printout the resulting list - after sorting
for k in num_list:
    print(k, end=", ")
print()
