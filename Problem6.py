# Problem6: Do...While loop - this loop have to run at east once
# the check of the condition if loop should be run one more time
# is done at the end of the loop - hence it runs at least one

# Guessing number game: guess a number between 1 an 10 : 1
# Guess a number between 1 and 10 : 7
# You guessed it

# My version of problem solving - it lacks an option to quit the
# guessing game
# import module for random numbers to be generated
import random
# assign a random number to a variable
rand_number = random.randrange(1, 10)
# run while loop for guessing of the random number
while True:
    try:
        # number from user input - changed into integer
        number = int(input("Guess a number between 1 and 10: "))
        # if statement to check if the number is the same as the
        # randomly generated
        if number == rand_number:
            # exit while loop if guessed
            break
        else:
            # print out the message to guess again
            print("Wrong, guess again: ")
    except ValueError:
        # print out statement to handle error in case of not a
        # number input
        print("You did not provide a number, "
              "guess a number between 1 and 10: ")
    except:
        # printout message for every other error
        print("Error")
print("You guessed it!")

# DB solution

# secret number assigned in code, not random
secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("You guessed it")
        break

