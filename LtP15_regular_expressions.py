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
# it printed out the "ape" 2 times but only the "ape" part for
# the word "apex" as it searches only for exact string

# to return full "apex" we can use "." after word that will
# be used to search for a string of "ape" plus 1 character or
# or space
allApes2 = re.findall("ape.", "The ape was at the apex")
# printout all "ape"s found
for i in allApes2:
    print(i)
