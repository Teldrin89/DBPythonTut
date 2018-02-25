# Problem5: How tall is the tree?
# Build a tree from "#" characters depending on how
# tall it should be (defined by user), for example if user types in 5:
#
#       #
#      ###
#     #####
#    #######
#   #########
#       #

# DB suggests to use 1 while loop and 3 for loops
# Pattern:
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 space  : 7 hashes
# 0 spaces : 9 hashes

# Need to do:
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height -1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and the hashes for each row
# 6. Print stump spaces and then 1 hash

# Get the number of rows for the tree
tree_height = input("Provide the height of our tree: ")
# Convert into integer
tree_height = int(tree_height)
# Get the starting spaces for the top of the tree
spaces = tree_height - 1
# There is one hash to start that will be incremented
hashes = 1
# Save stump spaces til later for bottom of the tree
stump_spaces = tree_height - 1
# Make sure the right number of rows are printed
# While loop to run through all levels of the tree height
while tree_height != 0:
    # Print the spaces, ending print with 'end=""' suggest
    # that next print statement should come up after this
    # one in the same line
    for i in range(spaces):
        print(' ', end="")
    # Print the hashes
    for i in range(hashes):
        print('#', end="")
    # Newline after each row is printed with nothing in it
    print()
    # Spaces is decremented by 1 each time
    spaces -= 1
    # Hashes is incremented by 2 each time
    hashes += 2
    # Decrement tree height each time to get out of the loop
    tree_height -= 1
# Print the spaces before stump and then the final hash
for i in range(stump_spaces):
    print(' ', end="")

print("#")
