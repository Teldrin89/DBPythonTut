# DB solution - a bit more elaborate and
# could be expanded for other equations
# plus the actual equation to be solved is embedded inside
# the code (but not the function)


def solve_eq(equation2):
    # Receive the string and split the string into variables
    x, operator, num1, equal, num2 = equation2.split()
    # Covert the string into ints
    num1, num2 = int(num1), int(num2)
    # Convert results into a string and
    # join it tp the string "x = "
    if operator == "+":
        return "x = " + str(num2 - num1)
    elif operator == "-":
        return "x = " + str(num2 + num1)
    elif operator == "*":
        return "x = " + str(num2 / num1)
    elif operator == "/":
        return "x = " + str(num2 * num1)
    # This is the enhanced version that can also cover the
    # reduction, multiplication and division


# Print out the results
print(solve_eq("x / 2 = 3"))

