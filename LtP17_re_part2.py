import re
from functools import reduce

# "look ahead" will look for a pattern to much but not return: (?=expression)
# example of a string
randStr = "One two three four"
# create a regular expression to look for all the letters and numbers of one or more in
# length separated by word boundary but without word boundaries (spaces)
regex = re.compile(r"\w+(?=\b)")
# the regular expression will look for any letter or number ("\w"), one or more ("+"),
# without the word boundaries "(?=\b")"
matches = re.findall(regex, randStr)

for i in matches:
    print(i)

print()

# "look behind" works similar as to "look ahead" but look for something before the text:
# (?<=expression)
# example of a string - take only words from it
randStr2 = "1. Bread 2. Apples 3. Lettuce"
# have to find a number, period and space before the part that are needed - words
regex2 = re.compile(r"(?<=\d.\s)\w+")
# the regular expression looks for a number ("\d"), period (".") and space ("\s") all
# inside the look behind sub-expression and then look for one ore more letters
matches2 = re.findall(regex2, randStr2)

for i in matches2:
    print(i)

print()

# example of "look ahead" and "look behind" in single regular expression
# string example
randStr3 = "<h1>I'm Important</h1> <h1>So am I</h1>"
# regular expression to grab only specific text in between headers
regex3 = re.compile(r"(?<=<h1>).+?(?=</h1>)")
# the regular expression looks behind for a string of "<h1>" and then takes one or more
# but with a lazy method and last looks ahead for closing header string "</h1>"
matches3 = re.findall(regex3, randStr3)

for i in matches3:
    print(i)

print()

# examples of negative "look ahead" and "look behind" to look for text that doesn't
# match the pattern:
# (?!expression) - negative look ahead
# (?<!expression) - negative look behind

# random string with items, numbers and prices
randStr4 = "8 Apples $34, 1 Bread $11, 1 Cereal $4"
# regular expression will look just how many items have been on the list
regex4 = re.compile(r"(?<!\$)\d+(?!,)")
# using the negative look behind in subexpression there is expression that should be
# omitted and then followed by whatever digits are there
# regular expression has been updated to take into account cases with 2 digits
# for the price of items (previously treated the second digit as separate and added it
# to number of items) - additional part is the negative look behind to ignore digits
# ending with ","
# still not working for more than 2-digit price and for the 2-digit price of last item
# as it is without comma - NEEDS ADDITIONAL WORK!
matches4 = re.findall(regex4, randStr4)
# printout the number of different items - length of matches list
print(len(matches4))
# convert list of strings to integers so that they then can be added for a sum of items
matches4 = [int(i) for i in matches4]
# use "reduce" function to sum all of the items found in the list
print("Total number of items: {}".format(reduce((lambda x, y: x + y), matches4)))
