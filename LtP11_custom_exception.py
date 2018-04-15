# it is possible to create a custom exception - it has to be
# inherited from the exception class


# create a new class for handling custom made exception - use
# inheritance of exception build in class
class DogNameError(Exception):
    # initialize the class with init function
    def __init__(self, *args, **kwargs):
        # use exception method to initialize
        Exception.__init__(self, *args, **kwargs)


# the try block contains the input from user
try:
    # ask for dog name
    dogName = input("What is your dogs name: ")
    # check if in any of the characters for dog name is a digit
    # using both if statement and for loop inside
    if any(char.isdigit() for char in dogName):
        # if there is a digit raise an exception and call
        # for custom exception created
        raise DogNameError
# exception handling block with custom exception to execute
except DogNameError:
    # printout the error message
    print("Your dogs name can't contain a number")
