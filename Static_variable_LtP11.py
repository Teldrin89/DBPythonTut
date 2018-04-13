# a static variable is a variable created inside a class but
# outside of any other methods; the use of static variable is
# that for any object created using the class in which this
# variable has been set up, it will be the same


# create a dog class
class Dog:

    # create a static variable - field outside of any method
    num_of_dogs = 0

    # initialize a class with init method with name
    def __init__(self, name="Unknown"):
        # assign name
        self.name = name

        # monitor each time the class will be used - increment
        # static variable num_of_dogs; to use the variable user
        # have o simply refer to it inside a class
        Dog.num_of_dogs += 1

    # create a static method that will print out the number
    # of dogs that have been created
    @staticmethod
    def getNumOfDogs():
        # printout the number of dogs
        print("There are currently {} dogs.".format(
            Dog.num_of_dogs))


# main function
def main():
    # create a number of dogs
    spot = Dog("Spot")
    doug = Dog("Doug")
    # the number of dogs stays the same for either of the 2 dogs
    spot.getNumOfDogs()
    doug.getNumOfDogs()


# call main
main()
