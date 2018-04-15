# to create a module you have to create a new separate python
# file with function - it has to be in the same directory that
# the other python file will be with import


# define a simple sum function
def getSum(*args):
    sum = 0

    for i in args:
        sum += i

    return sum
