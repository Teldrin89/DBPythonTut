# String functions

rand_string = "     this is an important string   "

# Function to remove additional spaces before the 1st word
rand_string = rand_string.lstrip()
# Function to remove additional spaces after the 1st word
rand_string = rand_string.rstrip()
# Function to remove additional spaces before and after
# the 1st word
rand_string = rand_string.strip()

# Function to capitalize first character in string
print(rand_string.capitalize())
# Function to capitalize full string
print(rand_string.upper())
# Function to convert all character to lower case
print(rand_string.lower())

# List example

a_list = ["bunch", "of", "random", "words"]
# Create a string by combining elements from list
print(" ".join(a_list))
# Separate words in string
a_list2 = rand_string.split()
for i in a_list2:
    print(i)

# Count how many times a string accounts in a string
print("How many is :", rand_string.count("is"))
# Find space where starts the given string
# (index of very first string)
print("Where is string :", rand_string.find("string"))
# Replace a part of string with the other
print(rand_string.replace("an ", "a kind of "))

# Additional functions

letter_z = "z"
num_3 = "3.14"
a_space = " "

# Check if string contains letters or numbers
print("Is z a letter or number: ", letter_z.isalnum())
# Check if string contains letters only
print("Is z a letter: ", letter_z.isalpha())
# Check if string contains numbers only
# (NOT working with floats)
print("Is 3 a number: ", num_3.isdigit())
# Check if letter is lowercase
print("Is z a lowercase ", letter_z.islower())
# Check if letter is upper
print("Is z a uppercase: ", letter_z.isupper())
# Check if string is space
print("Is space a space: ", a_space.isspace())


# As the "isdigit" is not working with floating point numbers
# We are going to CREATE a FUNCTION to cover that

def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False


print("Is Pi a float: ", isfloat(num_3))
