# import the module "sum" created in the same directory as this
# python script - import it as every other with "import" and the
# name of python file (without .py)
import sum

# use the getSum function from "sum" module
print("Sum: ", sum.getSum(1,2,3,4,5))

# there are 2 more different ways to import methods/functions:
# - user can use "from sum import getSum" - this will get only
#   one specific method
# - user can use "from sum import *" to get all the methods
