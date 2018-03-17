# Problem 13: create an array of dictionaries of customers
# DB solution
# Create a list
customer = []
# Create a loop
while True:

    # Yes or No question
    # Get input and make it work for y or n
    createEntry = input("Enter customer (Yes/No): ")
    # Gets 1st char from string and makes it lower case
    createEntry = createEntry[0].lower()
    # Check to leave loop - remember that to check the variable
    # content you need logical operator (hence "==")
    if createEntry == "n":
        break
    # Get customer data
    elif createEntry == "y":
        fName, lName = input("Enter customer name: ").split()
    # Added the scenario in which user puts neither "yes" nor "no"
    elif createEntry != "n" and createEntry != "y":
        print("You've put something wrong")
        break


    # Add customer data to list
    customer.append({"fName": fName, "lName": lName})

# Print customer data
for cust in customer:
    print(cust["fName"], cust["lName"])
