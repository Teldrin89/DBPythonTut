# iterable - it is a stored sequence of values (or put it
# simply it is a list of values); it also can act as an
# object that produce a single value at a time
# iterator - it is an object with a method "__next__" -
# that retrieves next value form a sequence of values

# create a sample string value
strSample = iter("Sample")
# printout the next character from string
print("Char: ", next(strSample))
# using the same command 2nd time is returning the next
# character from sample string
print("Char: ", next(strSample))


# create a class with iterator behavior
# create an alphabet class
class Alphabet:
    # initialize class with all letters and an index
    # that iteration will start with
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    # create iteration method of this class
    def __iter__(self):
        # return this object
        return self

    # define next method in this class
    def __next__(self):
        # create if statement to sto iteration only if
        # there is no more elements in string
        if self.index >= len(self.letters) - 1:
            # stop iteration exception
            raise StopIteration
        # increment value of index
        self.index += 1
        # return each character from string
        return self.letters[self.index]


# create a custom object and assign it to the class
alpha = Alphabet()
# loop for all letters in alpha using custom iteration
# from created Alphabet class
for letters in alpha:
    print(letters)

# through dictionary (which is iterable) it is possible
# to iterate without a method "keys"
# create a dictionary with 2 entries
name = {"fName": "Luke", "lName": "Cies"}
# run for loop with key as iterator through dictionary
for key in name:
    # printout the results
    print(key, name[key])
