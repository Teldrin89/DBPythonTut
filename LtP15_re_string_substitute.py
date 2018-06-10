# regular expression used to substitute strings with other
# strings

import re
# create a string with owl food
owlFood = "rat cat mat pat"
# compile 2 of the owl food from owlFood string
regex = re.compile("[cr]at")
# use substitute method to change the compiled strings
# from owlFood
owlFood = regex.sub("owl", owlFood)
# printout results
print(owlFood)
