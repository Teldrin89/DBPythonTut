# Ask the user to input their name and assign
# it to a variable named name

name = input('What is your name ')

# Print out hello followed by the name they entered

print('Hello ', name)

# Ask the user to input 2 values and store them in variables
# num1 and num2

num1, num2 = input('Enter 2 numbers: ').split()

# Convert the strings into regular numbers

num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum

summ = num1 + num2

# Subtract values and store in difference

difference = num1 - num2

# Multiply values and store in product

product = num1 * num2

# Divide values and store in quotient

quotient = num1 / num2

# Use modulus on the values to find the remainder

remainder = num1 % num2

# Print results

print("{} + {} = {}".format(num1, num2, summ))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
