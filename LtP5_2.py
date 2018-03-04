# How to deal with a situation that we get unknown number of
# arguments in the function


def sumAll(*args):
    # Because we don't know how many arguments we have
    # for the function we put splat (*) and args
    sum = 0
    for i in args:
        sum += i
    return sum


print("Sum : ", sumAll(1,2,3,4))


