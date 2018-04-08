# inheritance - all of the fields and methods can be inherit
# from previously created class - the class methods will
# be taken from is then called "superclass" and tha class that
# inherits from is called "subclass"


# define a super class - Animal
class Animal:
    # define initialization method - with several properties
    # like birth type, appearance and blooded type
    def __init__(self, birthType="Unknown",
                 appearance="Unknown", blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    # define a getter method for property
    @property
    def birthType(self):
        return self.__birthType

    # define a setter for property
    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    # define a getter method for property
    @property
    def appearance(self):
        return self.__appearance

    # define a setter for property
    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    # define a getter method for property
    @property
    def blooded(self):
        return self.__blooded

    # define a setter for property
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # define a magic method example - starts and ends with
    # 2 underscores - string magic method used to cast object
    # as  a string: whenever the object is cast it will print out
    # many detailed information
    def __str__(self):
        # it will return a defined string - name of animal and all
        # of the properties, a specific way to get a class name -
        # "type(self).__name__"
        return "A {} is {} it has {} it is {}".format(type(
            self).__name__, self.birthType, self.appearance,
                                                     self.blooded)

    # every getter, setter (or method in general) will be
    # inherited from Animal class in a new class - called Mammal
    # you can pu multiple different classes in the new one by just
    # adding them after "," like for example "Animal, Reptile"


class Mammal(Animal):
    # initialize the class with method, add correct
    # properties to method variables
    def __init__(self, birthType="born alive",
                 appearance="hair of fur",
                 blooded="warm blooded",
                 nurseYoung=True):
        # all methods defined from previous class - Animal
        # - can be called in this class
        Animal.__init__(self, birthType, appearance, blooded)
        # define new method - nurseYoung as it was not
        # defined in previous class
        self.__nurseYoung = nurseYoung

    # define a getter method for property - nurseYoung
    @property
    def nurseYoung(self):
        return self.__nurseYoung

    # define a setter for property - nurseYoung
    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # to make sure that this could overwrite the magic string
    # method we have to refer to the same method of super
    # class - remember to add "super()." - the "+" sign will
    # add this part to the string; in reference there is no
    # need for double underscore as the method is in the same
    # class that we are right now
    def __str__(self):
        return super().__str__() + " and it is {} they nurse" \
                                   "their young".format(
            self.nurseYoung)


# define one more class with animal type - reptile
class Reptile(Animal):
    def __init__(self,
                 birthType="born in an egg or born alive",
                 appearance="dry scales",
                 blooded="cold blooded"):

        Animal.__init__(self, birthType, appearance, blooded)

    # the function overloading - for most programming languages
    # if we want to create a method that will have an unknown
    # number of variables you would have to create each function
    # for different number of variables (or even type of variables)
    # and differentiate them by just the number of values
    # this example shows the function that would sum all using
    # only 2 integers
    # def sumAll(self, int, int, string): # commented
    # if you would like to add 3 integers you would have to add
    # one more to the list - still can name it the same, it will
    # be differentiated by just number of values used
    # def sumAll(self, int, int, int, string): # commented

    # in python you can define a function with unknown number
    # of values using splat option "*args"
    def sumAll(self, *args):
        sum = 0
        for i in args:
            sum += i

        return sum


# create a function that will get some object
def getBirthType(theObject):
    # it will printout the object name and use the method
    # "birthType" and regardless of the object, if given
    # method exists there it will execute
    print("The {} is {}.".format(type(theObject).__name__,
                                 theObject.birthType))


# once all classes have been created we call main function
def main():
    # create animal variable and call animal class and call one
    # of the methods and define birth type
    animal1 = Animal("born alive")
    # print out the birth type of our animal1
    print(animal1.birthType)
    # print out full magic method - string - about animal1
    print(animal1)
    # print out empty line
    print()
    # create a mammal1 variable and assign to it a mammal class
    mammal1 = Mammal()
    # print out the mammal1 variable birth type - there will be
    # already some values as we set up them as default
    print(mammal1.birthType)
    # print out string function on mammal1
    print(mammal1)
    # create a reptile variable and assign it to reptile class
    reptile1 = Reptile()
    # print out the birth type of reptile1 variable
    print(reptile1.birthType)
    # use the sum method defined in reptile class (assigned to
    # reptile1 variable) and show it can add :)
    print("The sum is = {}".format(reptile1.sumAll(1, 2, 3, 4)))

    # polymorphism - functions are going to accept any object
    # and expect that given object is going to be able to provide
    # the needed method to execute; the reason why is that in most
    # programming languages user defines variable type as the
    # variable is initialized and then given variable accepts
    # only specified type of data; in python the variable is
    # initialized and with putting a specific data inside it
    # will assign the type automatically (based on data put in)
    #
    # languages like c++ or java are statically typed (type
    # is defined at declaration of variable) and python is
    # dynamically typed (as variable type is defined at the
    # moment of assigning data)

    # call for the function that don't have specified object in
    # itself but rather takes it as an input
    getBirthType(mammal1)
    getBirthType(reptile1)


# call main function
main()
