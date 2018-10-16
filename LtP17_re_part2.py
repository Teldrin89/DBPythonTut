import re
# "look ahead" will look for a pattern to much but not return: (?=expression)
# example of a string
randStr = "One two three four"
# create a regular expression to look for all the letters and numbers of one or more in
# length separated by word boundary but without word boundaries (spaces)
regex = re.compile(r"\w+(?=\b)")
# the regular expression will look for any letter or number ("\w"), one or more ("+"),
# without the word boundaries "(?=\b")"
matches = re.findall(regex, randStr)

for i in matches:
    print(i)

print()

# "look behind" works similar as to "look ahead" but look for something before the text:
# (?<=expression)
# example of a string - take only words from it
randStr2 = "1. Bread 2. Apples 3. Lettuce"
# have to find a number, period and space before the part that are needed - words
regex2 = re.compile(r"(?<=\d.\s)\w+")
# the regular expression looks for a number ("\d"), period (".") and space ("\s") all
# inside the look behind sub-expression and then look for one ore more letters
matches2 = re.findall(regex2, randStr2)

for i in matches2:
    print(i)

print()

# example of "look ahead" and "look behind" in single regular expression
# string example
randStr3 = "<h1>I'm Important</h1> <h1>So am I</h1>"
# regular expression to grab only specific text in between headers
regex3 = re.compile(r"(?<=<h1>).+?(?=</h1>)")
# the regular expression looks behind for a string of "<h1>" and then takes one or more
# but with a lazy method and last looks ahead for closing header string "</h1>"
matches3 = re.findall(regex3, randStr3)

for i in matches3:
    print(i)

print()
