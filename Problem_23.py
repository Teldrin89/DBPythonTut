import re

# Problem 23:
# Use regular expressions to match email addresses
# from the list with set rules for what is an email
# address (just find how many there are):
# 1. 1 to 20 lowercase and uppercase letters, numbers,
#    plus ._%+- symbols
# 2. An @ symbol
# 3. 2 to 20 lower case and uppercase letters, numbers
#    plus .- symbols
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

# create a dummy list of emails, not all following the rules
emailList = "db@aol.com me@.com @apple.com db@.com"
# email = "db@.com"
# printout how many of email addresses there are that follow
# the rules using re.findall - specified characters in []
# brackets and number of characters in {} brackets
print("Email Matches: ", len(re.findall("[\w._%+-]{2,20}@"
                                        "[\w.-]{2,20}."
                                        "[A-Za-z]{2,3}",
                                        emailList)))

# some additional solution - mine - printout the email address
# that fulfills the criteria
# first, split string with all addresses and create a list
listOfEmails = emailList.split()
# run for loop by all email addresses from the list
for email in listOfEmails:
    # use re.search function with the same set of criteria
    if re.search("[\w._%+-]{2,20}@"
                 "[\w.-]{2,20}."
                 "[A-Za-z]{2,3}", email):
        # printout email address if criteria are met
        print("Email: ", email)
