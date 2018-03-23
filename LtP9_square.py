# Getters and setters - used to protect object from assigning bad
# field values also to provide improved output
# Create a class called square


class Square:
    # Initialize class with self, height and width
    def __init__(self, height="0", width="0"):
        # assign the variables: height and width
        self.height = height
        self.width = width

    # create a getter - @property to refer to individual variables
    # to get these values
    @property
    def height(self):
        # printout the resulting value - height
        print("Retrieving the Height")
        # __ - this way the value is protected
        return self.__height

    # define setter (height as setter) to protect height from
    # bad value setting - in this case it should be a number

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    # similar getter as in height case

    @property
    def width(self):
        print("Retrieving the Width")
        return self.__width
    # similar setter as in height case

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    # one more useful function to calculate the area of square

    def getArea(self):
        return int(self.__width)*int(self.__height)


# The main method - for running the function
def main():
    # assigning it to aSquare variable
    aSquare = Square()
    # for both "height" and "width" it is possible to call them
    # by their exact names (like without "()") because of the
    # property and setter option
    height = input("Enter Height: ")
    width = input("Enter Width: ")

    aSquare.height = height
    aSquare.width = width
    # Call out the height and width of square
    print("Height: ",aSquare.height)
    print("Width: ", aSquare.width)
    # Call out the area of square
    print("Area is: ", aSquare.getArea())


# Call main function to execute
main()
