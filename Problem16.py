# magic methods are surrounded by double underscores
# to show a few examples, here are some other standard magical
# methods like sum, multiplication and so on
# __eq__: Equal
# __ne__: Not Equal
# __lt__: Less Than
# __gt__: Greater Than
# __add__: Addition
# __sub__: Subtraction
# __mul__: Multiplication
# __div__: Division
# __mod__: Modulus
# Problem16: create a custom time class and using the magic methods
# add a second time object to 1st one - DB solution that will not
# really work if for example the number of seconds will exceed 120


# define a Time class
class Time:

    # initialize method for a Time class - defining the format
    # of the time - military type with 24hrs
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # string magic method - what will be return upon calling
    # this class
    def __str__(self):
        # formatting the values for minutes and seconds
        # to always have 2 digits
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute,
                                         self.second)

    # add magic method for other (new) time
    def __add__(self, other_time):
        # use the Time object already created to define a
        # new time that will be added to the 1st one
        new_time = Time()

        # Add seconds and correct if sum >= 60
        if (self.second + other_time.second) >= 60:
            # adding 1 minute to the 1st time object
            self.minute += 1
            # setting up new seconds with values from 1st and
            # 2nd time (minus the minute taken to minutes
            new_time.second = (self.second +
                               other_time.second) - 60
        else:
            # normal operation of adding seconds in case
            # together they are below 60
            new_time.second = self.second + new_time.second

        # Add minutes and correct if sum >= 60
        if (self.minute + other_time.minute) >= 60:
            # adding 1 minute to the 1st time object
            self.hour += 1
            # setting up new minutes with values from 1st and
            # 2nd time (minus the hour taken to hours)
            new_time.minute = (self.minute +
                               other_time.minute) - 60
        else:
            # normal operation of adding minutes in case
            # together they are below 60
            new_time.minute = self.minute + new_time.minute

        # Add hour and correct if sum >= 24
        if (self.hour + other_time.hour) > 24:
            # setting up new hour with values from 1st and
            # 2nd time (going over 0 if exceeding 24hrs)
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            # normal operation of adding hours in case
            # together they are below 24
            new_time.hour = self.hour + new_time.hour

        # REMEMBER to return a new_time object
        return new_time


# main function definition
def main():
    # definition of new variable using the Time class
    time1 = Time(1, 20, 30)
    # printing out the defined time
    print(time1)
    # definition of 2nd time variable using the Time class
    time2 = Time(24, 41, 30)
    # printing out the addition of both times using the add
    # magical method to add them and print to show results
    print(time1 + time2)
    # adding 2 time1 variables just to further validate the code
    print(time1 + time1)


# calling main function
main()
