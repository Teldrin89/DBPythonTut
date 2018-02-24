# Problem2: If age is 5 - go to kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater then 17 say go to college
# Try to complete with 10 or less lines

# My solution, DB seem to be similar - one more variable defining
# grade in his solution
age = eval(input("Please provide your age: "))
if age == 5:
    print("You are {}, go to kindergarten".format(age))
elif 17 >= age >= 6:
    print("You are {}, go to school, to grade {}".format(age, age-5))
elif age > 17:
    print("You are {}, go to college".format(age))
else:
    print("You are too young to go to school or did not provide a number.")
