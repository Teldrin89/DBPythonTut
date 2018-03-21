# Object Oriented programming - all seem t be similar, as in
# a real world we create objects that have attributes (like
# height, weight and favorite food) called in python FIELDS and
# capabilities (like for example a dog can run, walk and eat)
# called in python METHODS/FUNCTIONS
# Create a dog object using template - class (name with cap letter)
class Dog:
    # To initiate the class we use a function __init__
    # it hes by default a self value set - this allows to object
    # to be referred to itself (as in "my" for example "my weight")
    # the other variables are name, height and weight - all with
    # set default values
    def __init__(self, name = "", height = 0, weight = 0):
        # defined attributes of object
        self.name = name
        self.weight = weight
        self.height = height
    # defined the methods of object (functions)
    # a function that let the object run
    def run(self):
        print("{} the dog runs".format(self.name))
    # a function that let the object eat
    def eat(self):
        print("{} the dog eats".format(self.name))
    # a function that let the object to bark
    def bark(self):
        print("{} the dog barks".format(self.name))


# main function - outside of class - that calls a class to create
# object with set attributes = name, weight and height
def main():
    # setting out a do object named spot with set attributes
    spot = Dog("Spot", 66, 26)
    # using a method of said object - in this case the dog to bark
    spot.bark()
    # re-name of dog object
    bowser = Dog()
    bowser.name = "Bowser"
    bowser.bark()

# referring to execute the main function
main()
