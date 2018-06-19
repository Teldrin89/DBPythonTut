import re

# to match number use \d and to match anything
# but numbers use \D
# create random string with numbers
randStr = "12345"
# specific search for a digit (not specific digit)
print("Matches: ", len(re.findall("\d", randStr)))
# returns 5 - as there are 5 digits in selected string
# to return a specific digit it has to be specified
print("Matches: ", len(re.findall("\d{2}", randStr)))
# this print returns "2" as it was searched for and
# it is 2nd place of string; once the match was found it is no
# longer counted for (and the part before as well)

# to find a specific string of digits of specific length
# it is also possible to use the same function but looking
# for within a range of numbers
# create range of numbers - 5 sets of digits
numStr = "123 1234 12345 123456 1234567"
# to find string of digits with length between 5 and 7 use
# te re function "findall"
print("Matches: ", len(re.findall("\d{5,7}", numStr)))
# returns 3 as 3 last sets have number of digits
# between 5 and 7
