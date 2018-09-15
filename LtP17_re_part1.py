import re

# back reference allows to re-use the expression that proceeds it
# as an example put a random expression with 2 "cat" words
randStr = "that cat cat fell out of the window"
# to match for "cat" that have the exact same "cat" before create a regular expression
# with sub-match
regex = re.compile(r"(\b\w+)\s+\1")
# the created regular expression in parentheses will match each word separated with
# space, the next part "\1" means that the regular expression will choose only a word
# that has exactly the same word in front
# use findall function to find the specified expression in random string
matches = re.findall(regex, randStr)
# printout number of matches
print("Matches: ", len(matches))
# printout the match found
for i in matches:
    print(i)
# put empty line
print()
# a more real world example - taking a link from website but without bold tags
randStr2 = "<a href='#'><b>The link</b></a>"
# create a regular expression with compile function, matching bold tags, grabbing
# anything and taking the lest number of results
regex2 = re.compile(r"<b>(.*?)</b>")
# now to replace the link without bold parts: substitute in random string the
# regular expression found but using the back reference
randStr2 = re.sub(regex2, r"\1", randStr2)
# printout the resulting string
print(randStr2)
# put empty line
print()
# another example - given a phone number use regular expression to match number
# and change a final output for different format
randStr3 = "424-555-1212"
# create a regular expression that will look for a phone number in standard format
# using to subexpressions matching digits
regex3 = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
# substitute using the sub regular expression function and filling it with the
# new format for phone number
randStr3 = re.sub(regex3, r"(\1)\2", randStr3)
# printout the new format
print(randStr3)
# put empty line
print()
