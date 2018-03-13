# Problem 13: create an array of dictionaries of customers
# DB solution
# Create a list
customer = []
# Create a loop
while True:

    # Yes or No question
    # Get input and make it work for y or n
    createEntry = input("Enter customer (Yes/No): ")
    createEntry = createEntry[0].lower()
    # Check to leave loop
    if createEntry == "n":
        break
    # Get customer data
    else:
        fName, lName = input("Enter customer name: ").split()
    # Add customer data to list
    customer.append({"fName": fName, "lName": lName})

# Print customer data
for cust in customer:
    print(cust["fName"], cust["lName"])
