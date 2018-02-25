# Math strings, exceptions and do...while loops

# I user enters something that is not a number the code will loop
# until the user will put number
while True:
    try:
        number = int(input("Please enter a number: "))
        break
    # The exception to the while loop, if there will be string the
    # loop will be still going but we will print out statement
    except ValueError:
        print("You didn't enter a number")
    # The exception without a condition is not recommended but
    # applicable to cover all errors
    except:
        print("An unknown error occurred ")
print("Than you for entering a number")


