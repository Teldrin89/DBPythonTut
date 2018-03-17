# Reading and writing text to a file
import os

# One of greatest use of reading and writing files is to have access
# to the data even if the program finishes its working
# OS module helps with manipulating text files

# Starting with "with" ensures that the file will be closed when
# the code will finish work
# Mode "w" will overrate what is inside the file (if want to add
# things need to use "a")
# Encoding UTF-8 reference the ASCII method of storing characters
# /n represents a new line in document
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd "
                 "some more")
# After the file has been created and filled with 3 lines of
# text you can read it using the similar way - not explicitly
# writing a module means it automatically gonna "read"
# To read data there are several methods: readline() - going to read
# everything in single string (but only one line); read() -
# will read everything in single string (including all lines);
# readlines() - is going to return a list of all lines as strings
with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

# Check if file is close or not
print(myFile.closed)
# Check file name associated with myFile object
print(myFile.name)
# Check latest used mode of file - "r" -> read
print(myFile.mode)
# Rename file
os.rename("mydata.txt", "mydata2.txt")
# Remove a file
os.remove("mydata2.txt")
# Create a directory - had to comment creating when run 2nd time
# os.mkdir("mydir")
# Change into a directory
os.chdir("mydir")

print("Current directory: ", os.getcwd())
# Move up a directory
os.chdir("..")
print("Current directory: ", os.getcwd())
# Remove a directory
os.rmdir("mydir")
