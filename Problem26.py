import re

# Problem26 - take a random string with website addresses and convert them to URL
# as in example:
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='https://www.google.com'>www.google.com</a>
# use back reference substitution to make it work

randStr = "https://www.youtube.com http://www.google.com"

# create a regular expression to read from randStr
regex = re.compile(r"(https?://([\w.]+))")
# using the subexpression inside the regular expression string:
# - starting from "http" then "s" which is not always available hence "?"
# - inside another subexpression the website address starting from "w" will be taken
randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)

print(randStr)
