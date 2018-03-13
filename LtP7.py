# Dictionaries - are similar to lists but instead of sequential
# indexes they are structured with a key-value pairs

lukeDict = {"fName": "Luke", "lName": "Cieslak",
            "address": "321 Second St"}
# printout the value from a dictionary
print("My name is: ", lukeDict["fName"])
# substitute value inside a dictionary for given key
lukeDict["address"] = "123 Main St"
# add a key to dictionary
lukeDict["city"] = "Warsaw"
# Returns true or false after checking for a given key
print("Is there a city: ", "city" in lukeDict)
# Return list of values from dictionary
print(lukeDict.values())
# Returns list of keys from dictionary
print(lukeDict.keys())
# For loop to get both keys and values
for k, v in lukeDict.items():
    print(k, v)

# Get values associated with a key or return a default
print(lukeDict.get("lName", "Not Here"))
# Delete a key value
del lukeDict["fName"]
# Loop through dictionary keys
for i in lukeDict:
    print(i)

# Clear values from dictionary
lukeDict.clear()

# Create list to hold a dictionary
# First, create empty list
employees = []
# Then set up variables for first and last name to be put in
# Use split function to separate what is on the right and
# left side of whitespace
# Additional piece of code (as per DB suggestion) that is trying to
# handle exception error (in case someone provides only first name
# though probably it could look better (as it is still printing out
# empty list in case of an issue plus it's unwise to handle except
# without any condition)

while True:
    try:
        fName, lName = input("Enter Employee Name : ").split()
        # Append the values in new dictionary
        employees.append({"fName": fName, "lName": lName})
        break
    except:
        print("Only first name filled")
        break

# employees.append({"fName": fName, "lName": lName})
# printout
print(employees)

