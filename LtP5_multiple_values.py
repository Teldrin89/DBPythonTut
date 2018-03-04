# To receive a multiple values from a function you simply specify
# more than 1 of them and separate them with a comma
def mult_divide(num1, num2):
    # There may be an issue with num2 being assigned "0"
    # It safe to put some error exception handling (tried
    # here with "if" statement"
    if num2 != 0:
        return (num1 * num2), (num1 / num2)
    else:
        return (num1 * num2), "Error - denominator is equal to 0"


# The 2 values that will be returned from a function are assigned
# to 2 variables: mult and divide
mult, divide = mult_divide(5, 0)

# Print out the results
print("5 * 0 = ", mult)
print("5 / 0 = ", divide)

