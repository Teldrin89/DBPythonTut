# Problem 14: Using the Fibonacci sequence number generation
# function create a script to generate the full sequence up
# to the selected number of values
# My take on this problem - print out in loop (for loop used)


def fib(num):
    # What to return in case of 0
    if num == 0:
        return 0
    # What to return in case of 1
    elif num == 1:
        return 1
    # What to return in case of any other number
    else:
        # The result if a sum of 2 previous numbers
        result = fib(num - 1) + fib(num - 2)
        return result


# Ask how many points you need for the sequence
endNumber = input("How many numbers from Fibonacci "
                  "sequence: ")
# This conversion to integer could be done in input above
endNumber = int(endNumber)

# Loop while calling for each new number plus print results
for i in range(0, endNumber):
    print(fib(i))

# Print end statement
print("End of calc")

# DB take on that problem - only difference is the usage of
# while loop instead of for and there is one additional
# variable (that later is printed out)

# Initiation of variable to be used in while loop
k = 1
while k < endNumber:
    fibValue = fib(k)
    print(fibValue)
    k += 1

print("All done")
