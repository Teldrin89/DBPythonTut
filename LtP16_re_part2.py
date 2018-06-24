import re

# to match zero or one specific string use re.compile function and
# and a "+" with additional string to be matched and "?" that
# will be used to find either 0 or 1 of the specified additional
# string
# create a random string
randStr = "cat cats"
# use re.compile function to set a criteria to match both words
regex = re.compile("[cat]+s?")
# use re.findall on randStr to find both words using the regex
# criteria set before
matches = re.findall(regex, randStr)
# printout all matches find in random string
for i in matches:
    print(i)
print()

# to match 0 or more of set characters use "*"
# new random string
randStr2 = "doctor doctors doctor's"
# use re.compile to set the criteria
regex2 = re.compile("[doctr]+['s]*")
# use re.findall to get all matching results from random string
matches2 = re.findall(regex2, randStr2)
# printout the results
for j in matches2:
    print(j)
print()
