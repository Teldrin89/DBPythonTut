import re
# multiple lines string example for string boundaries finding - grab
# only 1st word of each line

# create a random string with multiple lines
randStr = '''Ape is big
Turtle is slow
Cheetah is fast
'''
# create a regular expression that will only take the 1st word
# of each line - use a special tool of re that will allow targeting
# of each line with "^" symbol: "(?m)" will define a multiline
# targeting, then "^" will define the beginning of string, ".*" will
# define any character and any number of those, "?" defines not to grab
# the biggest string of all (not greedy), the last one is "\s"
# that will define and of the word
regex = re.compile(r"(?m)^.*?\s")
# write all matches in "matches" variable
matches = re.findall(regex, randStr)
# printout the number of matches using "len" function
print(len(matches))
# printout the found words
for i in matches:
    print(i)

print()

# subexpressions are part of larger expression - if you want to match
# a larger block of string from a random string

# create a random string with a specific part that is needed to be
# found
randStr2 = "My number is 412-555-1212"
# create a regex expression with a subexpression: "412-" will be
# found in random string and then the specific subexpression will
# be taken "(.*) - so everything after
regex2 = re.compile(r"412-(.*)")
# write all matches in "matches" variable
matches2 = re.findall(regex2, randStr2)
# printout the number of matches using "len" function
print(len(matches2))
# printout the found words
for j in matches2:
    print(j)

print()
