# Regular expressions (Regex) are used to:
# 1. Search for a specific string in a large amount of data
# 2. Verify that a string has the proper format (e.g. email, phone)
# 3. Find a string and replace it with another string
# 4. Format data into the proper form for importing for example

# import regular expression module
import re
# search for word "ape" in another string
if re.search("ape", "The ape was at the apex"):
    # search returns true or false, put a msg in case it's true
    print("There is an ape")

# re.findall - a method to find all the matches
allApes = re.findall("ape", "The ape was at the apex")
# printout all "ape"s found
for i in allApes:
    print(i)

print()
# it printed out the "ape" 2 times but only the "ape" part for
# the word "apex" as it searches only for exact string

# to return full "apex" we can use "." after word that will
# be used to search for a string of "ape" plus 1 character or
# or space
allApes2 = re.findall("ape.", "The ape was at the apex")
# printout all "ape"s found
for i in allApes2:
    print(i)

print()
# create a regular string
theStr = "The ape was at the apex"
# use finditer in iterable to find the matches
for i in re.finditer("ape.", theStr):
    # span function will show the indexes - starting and ending
    # for the string in search
    locTuple = i.span()
    # printout starting and ending indexes
    print(locTuple)
    # printout the matched strings
    print(theStr[locTuple[0]:locTuple[1]])

print()
# square brackets are used to match any of the letters put
# in there
animalStr = "Cat rat mat pat"
# the letters put there are case sensitive (with lower case "c"
# the "Cat" would not be found
allAnimals = re.findall("[Crmfp]at", animalStr)
# printout all found strings
for i in allAnimals:
    print(i)

print()
# to search the range of letters use "-" in brackets
someAnimals = re.findall("[c-mC-m]at", animalStr)
# printout result that start with letters between "c" and "m"
# either upper or lower case
for i in someAnimals:
    print(i)
print()

# to find string that don't start with specific character use
# caret symbol "^"
notSomeAnimals = re.findall("[^Cr]at", animalStr)
# printout results
for i in notSomeAnimals:
    print(i)
