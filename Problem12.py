# Problem12: Create a multiplication table
# Create a multidimensional list from 1 to 9
# My approach for the problem solution

# Create empty list of lists (2D, 9x9)
multiplicationList = [[0] * 9 for i in range(9)]
# First for loop for putting numbers 1-9 in first row and column
for i in range(10):
    multiplicationList[0][i-1] = i
    multiplicationList[i-1][0] = i
# Second loop - for each row (i) and each column (i), multiply
# the numbers from first column and row
for i in range(10):
    for j in range(10):
        multiplicationList[i-1][j-1] = multiplicationList[0][i-1] \
                                       * multiplicationList[j-1][0]
# printout the results for double check
for i in multiplicationList:
    print(i)
print()

# DB solution - only 2 for loops
multTable = [[0] * 10 for i in range(10)]
# different range definition - from 1 to 10
for i in range(1, 10):
    for j in range(1, 10):
        multTable[i][j] = i * j

for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end=" ,")
    print()
