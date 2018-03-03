# Problem9: Cesar's cipher code
# Passing a message that will be encrypted
# For example we could shift all letters by 3
# (the "A" would be then "D")
# A - Z 65-90
# a - z 97 - 122

# Hints
# Use isupper() to decide which unicode to work with
# Add the key (number of characters to shift) and if
# the key is bigger or smaller than the unicode for
# A, Z, a, z increase or decrease by 26

message = input("Provide your message: ")
key = int(input("Provide the key (1-26): "))
# Prepare the secret message
secret_string2 = ""
original_string = ""
# Cycle through each character in the message
for char in message:
    # If it isn't a letter then keep it as it is
    if char.isalpha():
        # Get the character code and add shift amount
        char_code = ord(char)
        char_code += key
        # If uppercase then compare to uppercase unicode
        if char.isupper():
            # If bigger than Z subtract 26
            if char_code > ord("Z"):
                char_code -= 26
            # If smaller than A add 26
            if char_code < ord("A"):
                char_code += 26

        # If lowercase then compare to lowercase unicode
        # do similar as for uppercase
        else:
            if char_code > ord("z"):
                char_code -= 26
            if char_code < ord("a"):
                char_code += 26
    # Convert from code to letter and add to message
        secret_string2 += chr(char_code)

    else:
        secret_string2 += char

print("Encrypted message: ", secret_string2)

# To decrypt the same message we apply the
# same key with negative sign

key = -key

# Remember that next for loop have to go through
# secret message (not the original)
for char in secret_string2:
    # If it isn't a letter then keep it as it is
    if char.isalpha():
        # Get the character code and add shift amount
        char_code = ord(char)
        char_code += key
        # If uppercase then compare to uppercase unicode
        if char.isupper():
            # If bigger than Z subtract 26
            if char_code > ord("Z"):
                char_code -= 26
            # If smaller than A add 26
            if char_code < ord("A"):
                char_code += 26

        # If lowercase then compare to lowercase unicode
        # do similar as for uppercase
        else:
            if char_code > ord("z"):
                char_code -= 26
            if char_code < ord("a"):
                char_code += 26
        # Convert from code to letter and add to message
        original_string += chr(char_code)

    else:
        original_string += char

print("Decrypted message: ", original_string)


