# the "finally...else..." is another way of putting exceptions
# check in the code - finally is going to be used if you
# always want a portion of the code to be used whether you got
# an error or not

# create few pieces of data - prepared numbers for division
num1, num2 = input("Enter 2 values to divide: ").split()
# in try section put the division of 2 numbers
try:
    # divide 2 numbers
    quotient = int(num1)/int(num2)
    # printout the results of division
    print("{} / {} = {}".format(num1, num2, quotient))
# the exception to be handled is a no go for division by 0
except ZeroDivisionError:
    # printout the error message
    print("You can't divide by zero")
# the code to be executed if exception DOES NOT occur
else:
    print("You didn't raise an exception")
# the code to be executed in either conditions (with or
# or without an error)
finally:
    print("I execute no matter what!")
