#vars
correctAnswers = 0

#function
def question(text, solution):
    answer = input(text)
    if answer == solution:
        print("Correct!")
    elif answer.lower() == solution.lower():
        print("Capital Letters Next Time!")
    else:
        print("Nope! It's ", solution)

#spacing
print("______________________")
print("")

#welcome
print("Welcome To The Quiz!")
print("Try To Answer All Of Those Questions Correctly!")
print("")

#questions
question("1 - First Name Of Bart Simpson's Father: ", "Homer")
question("2 - Name Of Restaurant, Where SpongeBob Works: ", "Krusty Krab")
question("3 - Name Of First Episode Of Stranger Things: ", "The Vanishing Of Will Byers")
question("4 - Name Of Tiabeanie's Step Mother From Disenchantment: ", "Oona")
question("5 - Name Of One Of Main Characters From The Big Bang Theory That Has Been In Space: ", "Howard")

