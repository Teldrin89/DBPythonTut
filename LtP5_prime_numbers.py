# Return a list of prime numbers (prime number can
# be only divided by 1 and itself without reminder)
# For example 5 is a prime but 6 is not

# Ask the user for a max prime to search up to

# Use for loop and check if modulus is equal to 0
# A function for checking the modulus


def isPrime(num):
    # For loop to go through range of values
    # from 2 to max specified value
    for i in range(2, num):
        # Condition check if modulus is equal to 0
        if (num % i) == 0:
            # If that comes as positive we know it is not a prime
            # hence it is not a prime - False
            return False
    # In any other condition it is a prime - so True
    return True


def getPrime(max_number):
    # Function that will get prime numbers into a list
    # Create empty list
    list_of_primes = []
    # For loop to search for all numbers from 2 to max number
    for num1 in range(2, max_number):
        # Use the function created before if any given
        # number is a prime number
        if isPrime(num1):
            # Add number if it is a prime to the list
            # - use append method
            list_of_primes.append(num1)
    # The result of the function is a list of primes variable
    return list_of_primes


# Outside of functions we ask for a max number to search for prime
# numbers (at the same time change it to integer)
max_num_to_check = int(input("Search for prime numbers up to: "))
# We use the 2nd function to get the list of prime numbers
# up to the max number put before
list_of_primes = getPrime(max_num_to_check)
# Write the values of prime numbers from the list using for loop
for prime in list_of_primes:
    print(prime)
