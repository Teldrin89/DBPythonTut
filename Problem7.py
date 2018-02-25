# Problem7: Translate fom and to UNICODE
# Enter a string to hide in uppercase: HIDE
# Secret Message: 3547890
# Original Message: HIDE
# The code works only for upper case char because their
# unicode range is in between 65 and 90
# After changes in line 16 and 27 (adding and removing 23)
# it works for both lower and upper cases - although the
# resulting code is not exactly the one from unicode
# I changed it to run with 2 variables - one for changing back
# to normal string and one to store unicode values

# Input - Enter a string to hide in uppercase
hidden_message = input("Enter a string to hide "
                       "(in uppercase): ")
secret_string = ""
secret_string2 = ""
# Cycle through each character in the string
for char in hidden_message:
    # Store each character code in a new string
    secret_string2 += str(ord(char)-23)
    secret_string += str(ord(char))
    # Print Secret Message
print("Secret Message: ", secret_string)

# Cycle through each character code 2 at a time by
# incrementing by 2 each time
norm_string = ""
for i in range(0, len(secret_string2)-1, 2):
    # Get 1st and 2nd for the 2 digit number
    char_code = secret_string2[i] + secret_string2[i+1]
# Convert the code into characters and add them to a new string
    norm_string += chr(int(char_code)+23)
# Print Original Message
print("Original Message: ", norm_string)
