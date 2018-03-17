# Recursive function is a function that refers (calls) itself
# inside itself
# The example could be a factorial function: for example factorial
# of 3! = 3 * 2 * 1
# One of the most important part of recursive function is a return
# statement


def factorial(num):
    if num <= 1:
        # In case variable is 1 it returns 1
        return 1
    else:
        # The function is referred to inside the said function
        # Each time the function refers to itself it decrements
        # the variable it runs with until 1 - when it gets to
        # condition above
        result = num * factorial(num-1)
        return result


print("4! = ", factorial(4))

# For the example provided (4) the function goes like this:
# 1st: result = 4 * factorial(3) : 4*6
# 2nd: result = 3 * factorial(2) : 3*2
# 3rd: result = 2 * factorial(1) : 2*1

