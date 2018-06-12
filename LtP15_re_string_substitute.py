# regular expression used to substitute strings with other
# strings

import re
# create a string with owl food
owlFood = "rat cat mat pat"
# compile 2 of the owl food from owlFood string
regex = re.compile("[cr]at")
# use substitute method to change the compiled strings
# from regex
owlFood = regex.sub("owl", owlFood)
# printout results
print(owlFood)

# backslash special characters may pose some issues so
# regular expressions do solve them
# create a string with 2 backslashes
randStr = "Here is \\stuff"
# printout the found double backslash string using regex search
print("Find \\stuff:", re.search("\\stuff", randStr))
# the above print didn't find anything, the one below solves
# this problem by putting 2 more backslashes
print("Find \\stuff:", re.search("\\\\stuff", randStr))
# an easier and more elegant way to adjust search is to
# use raw string that won't treat backslashes as special
# characters
print("Find \\stuff:", re.search(r"\\stuff", randStr))

# to match any character using regex search we can use "."
# but to match period itself you have to backslash it
# create a few strings with and without periods
randStr2 = "F.B.I. I.R.S. CIA"
# use findall method to find any characters
# separated by periods
print("Matches: ", len(re.findall(".\..\..\.", randStr2)))

# example with new lines matching/searching/substitution
# create a long string with new lines
longStr = '''This is a long
string that goes
on for many lines
'''

# printout the string
print(longStr)
# remove the new lines by compiling using regex method
regex2 = re.compile("\n")
# now substitute the new lines with spaces in adjusted string
longStr = regex2.sub(" ", longStr)
# printout result
print(longStr)

# other whitespaces:
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

