import math

# The code for calculation of area of a given shape
# This time it will be done using the approach with many different
# functions (to avoid a lot of "if's") and the main function


def get_area(shape):
    # Function to decide what other function should be used to
    # calculate area based on what was provided
    # Change shape string to lower case letters to
    # avoid miss matching
    shape = shape.lower()
    # Check for shape - rectangle
    if shape == "rectangle":
        # Call rectangle function
        rectangle_area()
    # Check for shape - circle
    elif shape == "circle":
        # Call circle function
        circle_area()
    elif shape == "triangle":
        # Call triangle function
        triangle_area()
    elif shape == "parallelogram":
        # Call parallelogram function
        parallelogram_area()
    elif shape == "trapezoid":
        # Call trapezoid function
        trapezoid_area()
    # Cover any other case
    else:
        print("Please enter rectangle or circle")


def trapezoid_area():
    # Function for trapezoid area calculation
    # Get input data: base, top and height
    base = float(input("Enter the base value: "))
    top = float(input("Enter the top value: "))
    height = float(input("Enter the height: "))
    area = ((base + top) / 2) * height
    print("The area of the trapezoid is ", area)


def parallelogram_area():
    # Function for parallelogram ("romb") area calculation
    # Get input data: base and height
    base = float(input("Enter the base value: "))
    height = float(input("Enter the height: "))
    area = base * height
    print("The area of the parallelogram is ", area)


def triangle_area():
    # Function for triangle calculation
    # Get input: base and height
    base = float(input("Enter the base value: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print("The area of the triangle is ", area)


def rectangle_area():
    # Function for rectangle area calc
    # Get input: length and width
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    # Calculate the area of rectangle
    area = length * width
    # Print out the result
    print("The area of the rectangle is ", area)


def circle_area():
    # Function for circle area calc
    # Get radius for circle area calc
    radius = float(input("Enter the radius: "))
    # Calculate area - use math functions for pi and power
    area = math.pi * (math.pow(radius, 2))
    # Printout the area for circle
    print("The area of the circle is {:.2f}".format(area))


# Main function - the only thing it does is to get input and run
# designated function for area calculation
def main():
    shape_type = input("Get area for what shape: ")
    get_area(shape_type)


# Call for main function
main()
