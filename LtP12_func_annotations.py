# function annotations - it is possible to assign data
# attributes to both variables and returns of a created method
# the problem that then user may encounter is that these
# are for documentation purposes only - they are not enforced
# on data used


# define a random function with some set attributes for
# different variables
def random_fun(name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("Age: ", age)
    print("Weight: ", weight)
    # return a sentence with some of the input variables
    return "{} is {} years old and weighs {}".format \
        (name, age, weight)


# in case it is used as it should be it will produce a correct
# sentence
print(random_fun("Luke", 29, 71.5))
# in case of putting data that does not match the type defined
# it will still work - no errors - although the IDE marks them
# as warnings
print(random_fun(89, "Luke", "Cat"))
# print out the list of annotations for provided function
print(random_fun.__annotations__)
