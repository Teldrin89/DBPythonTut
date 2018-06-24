import re

# Problem 24:
# New lines in windows are sometimes represented by "\n"
# or sometimes by "\r\n" - create a regular expression
# that will grab each new line from string
randStr = '''Just some words 
and some more\r
and more
'''
# my idea of how to get number of lines in a string
print("Number of new lines: ", len(re.findall("[\n]", randStr)))
print()

# DB idea of solving the problem, regex created with set of
# criteria: some number of characters and spaces, followed by
# \r - either 0 or 1, followed by single new line expression
regex = re.compile("[\w\s]+[\r]?\n")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)
