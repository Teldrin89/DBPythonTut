# Fibonacci number - a sequence that adds a two previous numbers
# to create the next one, as example: 1, 1, 2, 3, 5, 8, 13 etc
# To calculate it this should be the recursive function:
# Fn = Fn-1 + Fn-2
# Additional conditions for F0 = 0 and F1 = 1

# print(fib(3))

# 1st : result = fib(2) + fib(1) : 2 + 1 = 3
# 2nd : result = (fib(1) + (fib(0)) + fib(0) : 1 + 0 = 1
# The function returns only the single number from Fibonacci
# sequence - the one specified by user


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


print(fib(10))
print(fib(3))
print(fib(4))
print(fib(5))
