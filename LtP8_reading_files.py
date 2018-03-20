import os

# Creating text file with 3 line of text (taken from previous
# python scrip)
with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd "
                 "some more")

# Opening of text file created as myFile
with open("mydata2.txt", encoding="utf-8") as myFile:
    # Initiation of variable for while loop
    lineNum = 1
    # The while loop that will check all lines until all lines
    # are read - used while as there may be different number
    # of lines
    while True:
        # Reading of each full line - up to the new line
        line = myFile.readline()
        # if line doesn't have any data the loop breaks
        if not line:
            break
        # print line, line number
        print("Line", lineNum, " : ", line, end="")
        # Mini-problem: print out the line split for each word
        # Split each line into list
        wordList = line.split()
        # Use len() for finding the number of words
        print("Number of words: ", len(wordList))
        # loop to count characters in word list
        # initiate variable
        charCount = 0
        # loop for all of the words in word list
        for word in wordList:
            # loop for all characters in word
            for char in word:
                charCount += 1

        # divide character count by len word list
        avgNumChar = charCount/len(wordList)
        # print out the average word length
        print("Avg Word Length: {:.2}".format(avgNumChar))

        # increment inside while loop
        lineNum += 1
