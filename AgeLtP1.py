# We'll provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 60 -> Important
# All others -> Not Important

# Receive age and store in age
# "eval" can automatically convert string into integer

age = eval(input("Enter age: "))

# and: If both are true it returns true
# or: If either condition is true then true
# not: Convert a true condition into false

# If age is both greater than or equal to 1 and less than or
# equal to 18 Important

if (age >= 1) and (age <= 18):
    print("Important Birthday")

# if age is either 21 or 50 Important

elif (age == 21) or (age == 50):
    print("Important Birthday")

# We check if age is less than 65 and then convert to false and
# vice versa

elif not(age < 65):
    print("Important Birthday")

# Else Not Important

else:
    print("Sorry Not Important")
