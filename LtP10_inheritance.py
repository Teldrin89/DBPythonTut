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
        self.birth = birthType
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

