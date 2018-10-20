# or conditional used to find different matches that then will be accepted or not
import re

# create a random string with different items - words and numbers
randStr = "1. Dog 2. Cat 3. Turtle"
# create a regular expression that will look for dog and cat out of the random string
regex = re.compile(r"\d\.\s(Dog|Cat)")
# to target 2 different words that were chosen they have to simply be put in parentheses
# with "|" that means "or"
# find the words chosen
matches = re.findall(regex, randStr)
# printout the results
for i in matches:
    print(i)

print()
