import re

# create a random string with multiple entries separated by tag
# for example a name tag
randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"
# create a regular expression that will take each name from the
# selected tag
regex = re.compile("<name>.*</name>")
# use findall regex method to find the specified regular expression
# from random string
matches = re.findall(regex, randStr)
# printout the results
for i in matches:
    print(i)

print()
# the results are not good - both tags have been printed out as the
# "*" is "greedy" and it has considered the 1st starting tag and last
# closing tag and printed out everything in between
# to make it work it has to be changed to "lazy" - put a "?" inside -
# it will match the smallest string in between
regex2 = re.compile("<name>(.*?)</name>")
matches2 = re.findall(regex2, randStr)

for j in matches2:
    print(j)

# to get just the names use a subexpressions - put the expression
# that is looked for in normal brackets - "(.*?)"
print()
