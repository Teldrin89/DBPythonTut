# lambda - it is a similar to "def" but it's not assigning the
# function to a name - that's why it's also referred to as a no-
# - name function - it only returns the function; usually it is
# used when user wants to use a quick simple function and want
# to avoid multiple names
# the basic syntax: "lambda arg1, arg2,...: expression use args"


# user may assign a lambda function to a name although IDE
# will show warning to use def in that case
sum = lambda x, y: x + y
# printout the result of lambda function
print("Sum: ", sum(4, 5))


# create a vote check function
can_vote = lambda age: True if age >= 18 else False
# print out the function result
print("Can vote:", can_vote(19))

# a power list lambda function example
power_list = [lambda x: x**2,
              lambda x: x**3,
              lambda x: x**4]
# print out the results for each power using the for loop
# within the list of lambda functions with 4 as "x"
for fun in power_list:
    print(fun(4))

# user may also store lambdas inside a dictionary
# use this approach to store data from 2 warriors fighting
# from one of the previous problem sets
# create a dictionary for different types of attack, lambda
# functions will simply print out the message for each type
attack = {"quick": (lambda: print("Quick Attack")),
          "power": (lambda: print("Power Attack")),
          "miss": (lambda: print("Missed Attack"))}
# pass manually one of the attack just check the dictionary
# how it works
attack["quick"]()
# import random module for some randomize in selection of
# attack types - usually put on top of script - hence the
# warning from IDE
import random
# use random.choice method from "random" module - this will
# choose a random item from a list - so the "list" method is
# used to convert attack dictionaries keys into a list
attack_key = random.choice(list(attack.keys()))
# this time the attack dictionary uses the random key from
# previous random choice method
attack[attack_key]()
