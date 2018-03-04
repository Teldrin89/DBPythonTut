# Problem10: Solve for "x", the code receives algebraic
# equation, for example "x + 4 = 9"
# Basic constrains for the code:
# - "x" will always be the 1st value received
# - you only deal wit addition

# My approach is the "minimalist" one - it does not really
# require a function to work as we know exactly what are the
# positions for exact numbers to be reduced from one another

# Receive the string and split the string into variables
equation = input("Provide equation to solve (with "
                 "'x' as first and using only addition: ")
equation_list = equation.split()
# Covert the string into ints
a = int(equation_list[4])
b = int(equation_list[2])
# The function for this specific algebraic equation


def addition_eq(num1, num2):
    return num1 - num2


# Printing out result with new function
print("The result is x = ", addition_eq(a, b))
