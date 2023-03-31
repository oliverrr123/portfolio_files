#vars
questionNumber = 0
end = 0
correct = 0

#spacing
print("_____________________")
print("")

#welcome
print("Welocme To The QUIZ!")
print("Try To Answer All Of Those Questions Correctly!")
print("")

#question 1
question1 = input("1 - First Name Of Bart Simpson's Father: ")

if question1 == "Homer":
    print("Correct!")
    questionNumber = 1
    correct = correct + 1
elif question1 == "homer":
    print("Capital Letter Next Time!")
    questionNumber = 1
    correct = correct + 1
elif question1 == "Homer Simpson":
    print("Correct!")
    questionNumber = 1
    correct = correct + 1
else:
    print("Nope! It's Homer!")
    questionNumber = 1

#question 2
if questionNumber == 1:
    print("")
    question2 = input("2 - Name Of Restaurant, Where SpongeBob Works: ")

    if question2 == "Krusty Krab":
        print("Correct!")
        questionNumber = 2
        correct = correct + 1
    elif question2 == "Krusty krab":
        print("Capital Letter Next Time!")
        questionNumber = 2
        correct = correct + 1
    elif question2 == "krusty krab":
        print("Capital Letters Next Time!")
        questionNumber = 2
        correct = correct + 1
    else:
        print("Nope! It's Krusty Krab!")
        questionNumber = 2

#question 3
if questionNumber == 2:
    print("")
    question3 = input("3 - Name Of First Episode Of Stranger Things: ")

    if question3 == "The Vanishing Of Will Byers":
        print("Correct!")
        questionNumber = 3
        correct = correct + 1
    elif question3 == "Vanishing Of Will Byers":
        print("There is 'The' At The Beggining")
        questionNumber = 3
        correct = correct + 1
    elif question3 == "The vanishing of Will Byers":
        print("Capital Letters Next Time!")
        questionNumber = 3
        correct = correct + 1
    elif question3 == "The vanishing of will byers":
        print("Capital Letters Next Time!")
        questionNumber = 3
        correct = correct + 1
    elif question3 == "the vanishing of Will Byers":
        print("Capital Letters Next Time!")
        questionNumber = 3
        correct = correct + 1
    elif question3 == "the vanishing of will byers":
        print("Capital Letters Next Time!")
        questionNumber = 3
        correct = correct + 1
    else:
        print("Nope! It's The Vanishing Of Will Byers!")
        questionNumber = 3

#question 4
if questionNumber == 3:
    print("")
    question4 = input("4 - Name Of Tiabeanie's Step Mother From Disenchantment: ")

    if question4 == "Queen Oona":
        print("Correct!")
        questionNumber = 4
        correct = correct + 1
    elif question4 == "queen Oona":
        print("Capital Letter Next Time!")
        questionNumber = 4
        correct = correct + 1
    elif question4 == "queen oona":
        print("Capital Letters Next Time!")
        questionNumber = 4
        correct = correct + 1
    elif question4 == "oona":
        print("Capital Letter Next Time!")
        questionNumber = 4
        correct = correct + 1
    elif question4 == "Oona":
        print("Correct!")
        questionNumber = 4
        correct = correct + 1
    else:
        print("Nope! It's (Queen) Oona!")
        questionNumber = 4

#question 5
if questionNumber == 4:
    print("")
    question5 = input("5 - Name Of One Of Main Characters From The Big Bang Theory That Has Been In Space: ")

    if question5 == "howard":
        print("Capital Letter Next Time!")
        end = 1
        correct = correct + 1
    elif question5 == "wolowitz":
        print("Capital Letter Next Time!")
        end = 1
        correct = correct + 1
    elif question5 == "howard wolowitz":
        print("Capital Letters Next Time!")
        end = 1
        correct = correct + 1
    elif question5 == "Howard":
        print("Correct!")
        end = 1
        correct = correct + 1
    elif question5 == "Wolowitz":
        print("Correct!")
        end = 1
        correct = correct + 1
    elif question5 == "Howard Wolowitz":
        print("Correct!")
        end = 1
        correct = correct + 1
    else:
        print("Nope! It's Howard Wolowitz")
        end = 1

#end
if end == 1:
    print("")
    print("Thanks For Playing!")
    print("Correct Answers: ")
    print(correct)
    print("")
    print("______________________")
    print("")


