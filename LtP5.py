# Python functions allow us to re-use part of code
# This makes the overall code shorter and easier to understand

# Function example: simple function that adds two numbers


def add_numbers(num1, num2):
    return num1 + num2


print("5 + 4 =", add_numbers(5, 4))

# Local variables - any variable created inside a
# function is a variable available only inside this function
# Global variable is created outside of any function
# Even if the global variable is passed inside the function
# it may not necessarily change


def change_name(name):
    name = "Luke"


name = "Derek"
# Trying to change name using function and global var
change_name(name)
print(name)
# Didn't change the name
# To make it work is to assign return for a function
# so it would pass some value


def change_name2(name):
    return "Luke"


# Assign a new name using function
name = change_name2(name)
print(name)
# It did change the name
# Another way to make it work is to refer
# inside a function a global variable
gbl_name = "Sally"
# The new function does not even need input variable


def change_name3():
    # Reference to global variable set up before function
    global gbl_name
    gbl_name = "Sammy"


change_name3()
print(gbl_name)

# A function without return value would return none


def get_sum(num1, num2):
    sum = num1 + num2


print(get_sum(5, 2))
