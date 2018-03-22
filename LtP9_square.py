# Getters and setters - used to protect object from assigning bad
# field values also to provide improved output
# Create a class called square


class Square:

    def __init__(self, height="0", width="0"):
        # assign the variables height and width
        self.height = height
        self.width = width

    # create a getter
    @property
    def height(self):
        print("Retrieving the Height")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("Retrieving the Width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def getArea(self):
        return int(self.__width)*int(self.__height)


def main():
    aSquare = Square()

    height = input("Enter Height: ")
    width = input("Enter Width: ")

    aSquare.height = height
    aSquare.width = width

    print("Height: ",aSquare.height)
    print("Width: ", aSquare.width)

    print("Area is: ", aSquare.getArea())


main()
