# To get the type of variable you can use type function
print(type(3))
print(type(3.14))

print(type("3"))
print(type('3'))

samp_string = "This is a very important string"

# You can get a specific character from string
print(samp_string[0])
print(samp_string[-1])

print(samp_string[3+5])
# You can get the length of the string
print("Length : ", len(samp_string))
# You can dissect the string to get just a part of it:
# from 8th index till end
print(samp_string[8:])
# from 0 to 4 index
print(samp_string[0:4])
# Concatenate strings
print("Green" + "Eggs")
# Multiply strings
print("Hello" * 5)
# Convert int into string
num_string = str(4)
# Cycle through each char in string
for char in samp_string:
    print(char)
# Cycle through char in pairs
for i in range(0 , len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])

# Computers assign characters through UNICODE
# A - Z 65 - 90
# a - z 97 - 122

print("A = ", ord("A"))
print("97 = ", chr(97))

