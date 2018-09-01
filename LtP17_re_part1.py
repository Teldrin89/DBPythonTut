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
