# Problem 17:
# - create a file named "mydata2.txt" - put any type of data
# - use methods from LtP8 how to open a file without "with"
#   (open in "try" block)
# - catch FileNotFoundError
# - in "else" print contents of the file
# - in finally print out some msg that will always be on screen
# - try to open nonexistent file mydata3.txt - test

# create a try block
try:
    # inside open file using built in method open, by default
    # it is set to read, remember about encoding format
    my_file = open("mydata2.txt", encoding="utf-8")
# create an except block for handling error - in particular
# the error which will handle the missing of file
# define the error as variable "ex"
except FileNotFoundError as ex:
    # printout msg in case of an exception
    print("That file was not found")
    # printout additional information about the exception
    print(ex.args)
# create an else block - in case it finds the set file
else:
    # printout the information from text file - read function
    # of assigned variable for the file open method
    print("File: ", my_file.read())
    # close the file
    my_file.close()
# create a "finally" block
finally:
    # printout the massage that will be shown regardless if
    # the file has been found or not
    print("Finished working with exception handling")
