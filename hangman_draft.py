from __future__ import print_function
from random import randint
import re


WORDS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Python", "Sushi"]

HANGMAN_STAGES = [
    """"
------
|    |
|
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|   -+-
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-
|
|
|
|
|
------
""",

""""
------
|    |
|    0
|  /-+-/
|    |
|
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    |
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   /
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   / \\
|
|
------
"""
]


NUM_STAGES = len(HANGMAN_STAGES)

print ("You get " + str(NUM_STAGES) + " guesses!!")

#Randomly select an index value, in order to select the word in the WORDS list
randomIndex = randint(0, len(WORDS)-1)
hangmanWord = WORDS[randomIndex]

#print ("Ans: " + str(hangmanWord))

decodedValue = ""
for index in range(0,len(hangmanWord), 1):
    print ('_ ', end='')
    decodedValue = decodedValue + "_"
    index +=1

#Convert all letters to UPPER CASE for easier comparison
hangmanWord = hangmanWord.upper()

current_wrong = 0
so_far = "-"*len(hangmanWord)

#print ("\n" + hangmanWord)

while current_wrong <= NUM_STAGES and so_far != hangmanWord:
    value = raw_input("\nGuess a letter: ")
    #Convert the character to UPPER to match the HANGMAN word case (Upper)
    value = value.upper()

    #Determine if the character exists in the hangman word
    if value in hangmanWord:
        print ("Yay! Your letter %s is in the word." %value)
        newWord = ""

        for i in range(0, len(hangmanWord)):
            #print (str(i) + "==>" + str(hangmanWord[i]))
            if value == hangmanWord[i]:
                #print("Got here 1")
                newWord = newWord + value
                #print (newWord)
            else:
                #print("Got here 2")

                newWord = newWord + so_far[i]
                #print (newWord)

        so_far = newWord
        print ("Your Current Word is: " + so_far)

    else:
        print (HANGMAN_STAGES[current_wrong])
        current_wrong += 1
        print (so_far + "\n")


if current_wrong > NUM_STAGES:
    print ("You LOST")
else:
    print ("You guessed the word: " + hangmanWord + "!!!")