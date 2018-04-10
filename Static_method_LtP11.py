# The static method allows access to it without the need to
# initialize the class (which means user may be able to execute
# them with no object)


# create a class called sum
class Sum:
    # add a static method decorator to indicate that this method
    # will be static
    @staticmethod
    def getSum(*args):
        # the method uses splat - meaning it can be fed with
        # any number of variables
        # initialize the sum variable
        summ = 0
        # sum all of the values in method arguments using for loop
        for i in args:
            summ += i
        # return the sum value
        return summ


# create main function
def main():
    # call for static method within the Sum class but without
    # creating any object and print out result
    print("Sum: ", Sum.getSum(1, 2, 3, 4, 5))


# call main function
main()
