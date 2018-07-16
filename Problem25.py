import re
# Problem 25: use a subexpression to find only the specific phone
# numbers from several numbers provided in a string (without a area
# code number)

# create a random string with several phone numbers
randStr2 = "412-555-1212 412-555-1213 412-554-1214"
# create a regex expression with a subexpression that will be looking
# for only a specific phone numbers: use the number of characters
# as a subexpression definition - 8 characters
regex2 = re.compile(r"412-(.{8})")
# write all matches in "matches" variable
matches2 = re.findall(regex2, randStr2)
# printout the number of matches using "len" function
print(len(matches2))
# printout the found numbers
for j in matches2:
    print(j)

print()

# in case of trying to separate 2 pieces of data from single random
# string it is possible to use more then once a subexpression

# create a random string with single number but trying to get 2 parts
# of the number as 2 results
randStr = "My number is 412-555-1212"
# create a regular expression with 2 subexpressions
regex = re.compile(r"412-(.*)-(.*)")
# write all matches in "matches" variable
matches = re.findall(regex, randStr)
print(type(matches))
print(len(matches))
# printout the individually found matches
print(matches[0][0])
print(matches[0][1])
