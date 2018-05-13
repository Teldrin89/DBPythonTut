# Problem 21: Create a class that returns values from
# the Fibonacci sequence each time next is called
# Sample output:
# Fib :1
# Fib :2
# Fib :3
# Fib :5


# create a Fibonacci class
class Fib:
    # initialize class with 2 first numbers of the
    # Fibonacci list: 0 and 1
    def __init__(self):
        self.first = 0
        self.second = 1

    # create iteration method of this class
    def __iter__(self):
        # return this object
        return self

    # define next method in this class
    def __next__(self):
        # create a Fibonacci number variable that will
        # always be the latest one (so sum of 2 previous
        # ones)
        fibNum = self.first + self.second
        # assign the new value as new first - previous
        # second
        self.first = self.second
        # assign the new value as new second from the list
        self.second = fibNum
        # return Fibonacci number
        return fibNum


# assign the class to a variable
fibSeq = Fib()
# run the for loop to get several numbers from Fibonacci
# list
for i in range(10):
    print("Fib: ", next(fibSeq))
