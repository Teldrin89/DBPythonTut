# Problem 13: create an array of dictionaries of customers
# My solution - not really good
customers = []
question = input("Enter customer (Yes/No): ")

while question == "Yes":
    fName, lName = input("Enter Employee Name : ").split()
    customers.append({"fName": fName, "lName": lName})
    question = input("Enter customer (Yes/No: ")

number = len(customers)
print(number)
if number != 0:
    for i in range(number):
        print(customers[i])

