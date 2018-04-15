# exceptions are going to be triggered when there will be errors
# or when user specify - the handling is to find an exception and
# then the code will stop and execute the part that handles the
# specific error
# to handle exceptions user may use "try...except..." method
# put the code that the error may occur in "try" block
try:
    # create a list with 3 elements
    aList = [1,2,3]
    # printout the element from index 3 - which is not
    # existing in the provided list prompting an error
    print(aList[3])
# to handle the exception put what should be done in case
# of the index error exception block
# you can handle multiple different exception types in single
# exception: "except (IndexError, NameError)"
except IndexError:
    # it will printout a plain and simple text instead of
    # a bunch of errors and code
    print("Sorry that index doesn't exist")
# user may put plain except to handle all errors - but it's
# not recommended
except:
    print("Unknown error occurred")
