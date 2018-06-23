import re

# to match any single letter: \w : [a-zA-Z0-9_]
# to match anything that isn't a thing that is inside
# the string: \W: [a-zA-Z0-9_]

# try to use the regular expression string finding
# functions to confirm for example if provided string is
# a phone number

# telephone number example
phnNum = "444-555-1212"

# use the search function to determine if the provided
# string is composed with either letters or numbers with
# specific number of each in between spaces
if re.search("\w{3}-\w{3}-\w{4}", phnNum):
    # printout msg in case it's true
    print("It is a phone number")
# for that particular case a \d would be better as it
# would validate only digits that should be used in
# phone number
print()

# use regular expression functions to check if the
# first name is valid - the set conditions is to contain
# between 2 and 20 characters
if re.search("\w{2,20}", "Lucas"):
    print("That is a valid name")
print()

# to check for whitespaces use "\s" - use it verify if
# first and last name was provided, both wih 2 to 20
# characters
if re.search("\w{2,20}\s\w{2,20}", "Richard Feynman"):
    print("It is valid")
print()

# to match one or more characters we use "+" sign
# use findall function to find all matches of "a"
# followed by one or more characters
print("Matches: ", len(re.findall("a+", "a as ape bug")))
# the results show 3 matches as the first one is a letter
# "a" followed by whitespace
