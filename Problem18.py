# Problem 18:
# - create a function, that receives a list and a function
# - the function passed will return True or False if a list
#   value is odd
# - the surrounding function will return a list of odd numbers


# define a function that will check if the provided number
# is odd - return either true or false
def odds(num2):
    # use the modulus in built method and if statement
    if num2 % 2 == 0:
        # return if odd
        return False
    else:
        # return if even
        return True


# define a function that will use a list of numbers and the
# other function - the one to determine odd numbers
def list_of_nums(list, function):
    # define a list variable for odds only
    num_list = []
    # run a "for" loop through all numbers from provided list
    # of numbers - 1st variable of new function
    for i in list:
        # check the return value from the provided function -
        # in this case it will be the "odds" function for
        # which the return can be either true of false
        # (hence no comparison of function result
        if function(i):
            # this if statement will be completed only in
            # case of "True" - it will append a list of
            # numbers with only odd values
            num_list.append(i)
    # the return of the function will be an odd numbers list
    return num_list


# a list of numbers created to be provided to the function
# in this case a simple 1-20 range (without 20!)
a_list = range(1, 20)

print(list_of_nums(a_list, odds))
