# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their
# investment +  their investment * interest rate is
# Print out the earnings after a 10 year period

# My solution
investment = input("Please provide your investment ammount: ")
investment = float(investment)
interest_rate = 0.01

for i in range(1, 11):
    if i == 1:
        earnings = investment + (investment * interest_rate)
    elif i > 1:
        earnings = earnings + (earnings * interest_rate)

print("Your earnings after 10 years is {:.2f}".format(earnings))

# DB solution - different as in no if statement (used the same
# variable) and the interest rate provided by the user
# Ask for the the money invested + the interest rate
money = input("How much to invest: ")
interest_rate = input("Interest rate: ")

# Convert the value to a float
money = float(money)

# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01

# Cycle through 10 years using the for loop range from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)

# Output the results
print("Investment after 10 years: {:.2f}".format(money))
