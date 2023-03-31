from os import system
import time

def miss(number):
    if number == 0:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    if number == 1:
        print("")
        print("")
        print("")
        print("")
        print("")
        print(" _____")
    if number == 2:
        print("")
        print("")
        print("")
        print("")
        print(" _____")
        print("/_____\ ")
    if number == 3:
        print("")
        print("   |")
        print("   |")
        print("   |")
        print(" __|__")
        print("/_____\ ")
    if number == 4:
        print("    ______")
        print("   |")
        print("   |")
        print("   |")
        print(" __|__")
        print("/_____\ ")
    if number == 5:
        print("    ______")
        print("   |_/")
        print("   |")
        print("   |")
        print(" __|__")
        print("/_____\ ")
    if number == 6:
        print("    ______")
        print("   |_/   |")
        print("   |")
        print("   |")
        print(" __|__")
        print("/_____\ ")
    if number == 7:
        print("    ______")
        print("   |_/   |")
        print("   |     O")
        print("   |")
        print(" __|__")
        print("/_____\ ")
    if number == 8:
        print("    ______")
        print("   |_/   |")
        print("   |     O")
        print("   |     |")
        print(" __|__")
        print("/_____\ ")
    if number == 9:
        print("    ______")
        print("   |_/   |")
        print("   |     O")
        print("   |    /|\ ")
        print(" __|__")
        print("/_____\ ")
    if number == 10:
        print("    ______")
        print("   |_/   |")
        print("   |     O")
        print("   |    /|\ ")
        print(" __|__  / \ ")
        print("/_____\ ")
    
print("______________________")
print("")
print("")
print("")

secretWord = input("Type in the word you want your opponent to guess: ")

system('cls')

findingLetterCounter = 0

wordGuessCounter = 0
wordGuess = []
for x in range(len(secretWord)):
    wordGuess.append("_")
    wordGuessCounter += 1
wordGuessStr = str(wordGuess)

wordCounter = 0
word = []
for x in range(len(secretWord)):
    word.append(secretWord[wordCounter])
    wordCounter += 1
wordGuessCounterStr = str(wordGuessCounter)

winCounter = 0

wordGuessPrintCounter = 0

usedWrongLetters = []

lives = 0

win = False
death = False

guessing = True
while guessing:
    system("cls")
    miss(lives)
    print("")
    print("Used wrong letters: ")
    print(usedWrongLetters)
    print("")
    print(wordGuess)
    guessInput = input("Guess letters: ")
    if guessInput in secretWord:
        for x in range(len(secretWord)):
            if guessInput == secretWord[findingLetterCounter]:
                wordGuess[findingLetterCounter] = guessInput
            findingLetterCounter += 1

        if word == wordGuess:
            win = True
            guessing = False

    else:
        usedWrongLetters.append(guessInput)
        lives += 1
        if lives == 10:
            death = True
            guessing = False
    findingLetterCounter = 0

while win:
    system("cls")
    print("")
    print("You Won!")
    print("")
    print(f"The word was '{secretWord}'")
    print("")
    print("Used wrong letters:")
    print(usedWrongLetters)
    print("")
    time.sleep(100)

while death:
    system("cls")
    miss(10)
    print("")
    print("You Died!")
    print("")
    print(f"The word was '{secretWord}'")
    print("")
    print("Used wrong letters:")
    print(usedWrongLetters)
    print("")
    time.sleep(100)
    





#
#
#
#
#
#  _____

# 
# 
# 
# 
#  _____ 
# /_____\ 

#
#    |
#    |
#    |     
#  __|__
# /_____\ 

#     ______
#    |
#    |   
#    |  
#  __|__
# /_____\ 

#     ______
#    |_/
#    |   
#    |  
#  __|__
# /_____\

#     ______
#    |_/   |
#    |
#    |     
#  __|__
# /_____\

#     ______
#    |_/   |
#    |     O
#    |     
#  __|__
# /_____\

#     ______
#    |_/   |
#    |     O
#    |     |
#  __|__
# /_____\

#     ______
#    |_/   |
#    |     O
#    |    /|\
#  __|__
# /_____\

#     ______
#    |_/   |
#    |     O
#    |    /|\
#  __|__  / \
# /_____\
