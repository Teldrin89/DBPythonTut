# Problem8: Create an acronym from given string from user
# Convert them to full upper case

# My approach with DB guidelines,
# probably could be done with one less for loop

# Ask for a string
new_string = input("Please provide a string: ")
# Convert string to uppercase
new_string = new_string.upper()
# Convert the string into a list
new_list = new_string.split()
new_acronym =""
# Cycle through the list
for i in new_list:
    # Get the 1st letter of the word and eliminate the newline
    dummy_list = i.split()
    for j in dummy_list:
        # new_acronym += j
        new_acronym += j[0:1]
# Add a newline
print("The acronym of provided string: ", new_acronym)

# The only one "for" loop used by DB and printed on the spot
# (while adding characters)
for word in new_list:
    print(word[0], end="")

print()
