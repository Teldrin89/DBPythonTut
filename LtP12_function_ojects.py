# create a simple function for multiplication by 2
def mult_by_2(num):
    return num*2


# the function can be assigned to a variable
times_two = mult_by_2
# then user may use the variable to run said function
print("4 * 2 = ", times_two(4))


# the function can be passed into a function
def do_math(func, num):
    return func(num)


# printout the value by using the function within a function
# - without attribute - and then add attribute to the outside
# function
print("8 * 2 = ", do_math(mult_by_2, 8))


# create a dynamically generated function inside a function
# and return it to the outside function

# define the outside function
def get_fun_mult_by_num(num1):
    # define inside function - dynamically generated
    def mult_by(value):
        # return the multiplication based on the number put in
        # outside function and the argument of inside one
        return num1 * value
    # return the function inside a function
    return mult_by


# assign a function to a variable
generated_func = get_fun_mult_by_num(5)
# print out the the generated functions results
print("5 * 10 = ", generated_func(10))

# embed the function in a data structure
list_of_func = [times_two, generated_func]
# print out the result of multiplication by referring to
# functions inside a list - using index 1 user refer to 2nd
# function - generated_func - and add parameter in second
# parentheses - here it is 9
print("5 * 9 = ", list_of_func[1](9))
