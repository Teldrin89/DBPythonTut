# Problem19:
# Find an easy way to generate a list of "heads" and "tails"
# (use "H" and "T" chars) then store them in a list and output
# the number each side of a coin has been selected (used to
# verify how the random generators are working)
# Example output:
# Heads: 46
# Tails: 54
# import random module to use the random.choice method
import random
# create a list to be populated with results
coin_list = []
# run a for loop for predefined number of iterations - 100
for i in range(1, 101):
    # append list with either "heads" or "tails" based on the
    # random.choice method result for provided list: "H", "T"
    coin_list += random.choice(["H", "T"])

# printout the result in agreed format
print("Heads: ", coin_list.count("H"))
print("Tails: ", coin_list.count("T"))
