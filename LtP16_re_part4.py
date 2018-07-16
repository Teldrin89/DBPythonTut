import re
# word boundaries can be used to define where a specific word
# starts and ends - "\b" both defines start and end of word

# create a random string with multiple entries of a word that will
# be put in boundaries
randStr = "ape at the apex"
# create a regular expression that will only take the word in
# boundaries - "r" defines a raw string with set boundaries
# in between "\b"
regex = re.compile(r"\bape\b")
# use findall regex method to check the number of found words
matches = re.findall(regex, randStr)
# printout the number of matches
print(len(matches))
# printout the found words
for i in matches:
    print(i)
# the result is only a single entry of "ape" as the next string that
# would match "ape" is inside a whole word "apex"
print()

# to define boundaries for a string there are 2 symbols to be used:
# ^ - defines the beginning of the string
# $ - defines the ending of the string

# prepare a random string that will be searched - finding all up to
# a specific character
randStr2 = "Match everything up to @"
# create a regular expression that will take only string up to the
# the "@" symbol: "r" defines a raw string, then "^" defines a
# beginning of the string, then "." that defines any character, the
# "*" that defines any number of any string and then in square
# brackets we put the "^" and symbol that we want to end with
regex2 = re.compile(r"^.*[^@]")
# write the found string
matches2 = re.findall(regex2, randStr2)
# printout the found string
for j in matches2:
    print(j)
# this example will only work if the character on which we want to
# end is at the end of given random string
print()

# prepare a random string that will be searched - finding all without
# the 1st character of the string (and space)
randStr3 = "@ Get this string"
# create a regular expression that will take only end of the string
# ignoring "@" symbol: "r" defines a raw string, then "^" inside a
# square bracket (to be ignored) put "@\s" to ignore "@" and space
# after, then "." to search for any character and "*" for any number
# of any character and in the end "$" defining end of the string
regex3 = re.compile(r"[^@\s].*$")
# write the found string
matches3 = re.findall(regex3, randStr3)
# printout the found string
for j in matches3:
    print(j)

print()
