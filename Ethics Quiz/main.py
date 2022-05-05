# May 4 2022
# Main

import sys
import os
import time
import tkinter as tk

master = tk.Tk()

def mainMenu():
    print("Hello, please choose what you want.")
    print("[1] Information")
    print("[2] Take the quiz")
    print("[3] Quit")

    selection = int(input("Enter choice:\t"))
    if selection == 1:
        information()
    elif selection == 2:
        newGame()
    elif selection == 3:
        exit
    else:
        print("Invalid choice. Enter a number 1-3!")
        mainMenu()

def information():
    print("Hello")
    time.sleep(2.5)
    print("Sending you back to the menu...")
    mainMenu()

def newGame():
    
    guesses = []
    correctGuesses = 0
    questionNum = 1

    for key in questions:
        print("-----------")
        print(key)
        for i in options[questionNum - 1]:
            print(i)
        guess = input("Please enter (A, B, C, D):\t")
        guess = guess.upper()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(key), guess)
        questionNum += 1
    
    displayScore(correctGuesses, guesses)
#-----------------
def checkAnswer(answer, guess):
    
    if answer == guess: 
        print("You are correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

#-----------------
def displayScore(correctGuesses, guesses):
    print("-------------")
    print("RESULTS")
    print("-------------")
    
    print("Answers: ", end = "")
    for i in questions:
        print(questions.get(i), end = " ")
    print()

    print("Guesses: ", end = "")
    for i in guesses:
        print(i, end = " ")
    print()

    score = correctGuesses
    print("Your score is: {}!".format(score))

    

#-----------------
def playAgain():
    response = input("Do you want to play again?: (Yes or No):\t")
    response = response.upper()

    if response == "YES" or response == "Y":
        mainMenu()
    else:
        return False

#-----------------
def bye():
    print("Goodbye!")
    exit

#-----------------

questions = {
 "What is utilitarianism?: ": "A",
 "What is deontology?: ": "C",
 "Moral ethics scenario: Someone hacks your computer to take information with the intent to do harm. You are sad because someone did this as a selfish act without any good intentions. What moral philosophy are they most likely to follow? ": "A",
 "What does ICT stand for?: ": "C",
 "What is ethics?: ": "B",
 "What is a big issue in computer ethics? ": "D",
 "What is ICT?: ": "D",
 "Which of these are not in the Ten Commandments of Computer Ethics?: ": "A"
}

options = [["A. It is the moral philosophy of maximising happiness and minimizing pain.", "B. It is the moral philosophy of thinking that something is good if the intentions are good, rather than the result.", "C. It is the belief that there is only one right way to do something.", "D. It is the belief that only one person should have authority in a given setting."], 
          ["A. It is the moral philosophy of thinking optimistically, no matter what situation you are in.", "B. It is the moral philosophy that you should think pessimistically so you do not get hurt by unrealistic expectations.", "C. It is the moral philosophy of believing that the characteristics of an action contribute to if it is good, rather than the result of said action.", "D. It is the belief that you cannot control your life path and that it is chosen for you."],
          ["A. Utilitarianism", "B. Deontology", "C. None of the above", "D. All of the above"],
          ["A. Information and Critical Thinking", "B. Interests towards Computer Technology", "C. Information and Communications Technology", "D. Intellectual Communications Technology"],
          ["A. It is ones religion and beliefs about cosmology and something greater than human life.", "B. It is the moral discipline about what is good and what is bad.", "C. It is the steps someone takes to build a proper and successful life.", "D. It is the social skills of an individual and how an individual interacts with others."],
          ["A. Internet privacy", "B. Piracy", "C. Harmful actions online", "D. All of the above"],
          ["A. It is a thinking skill set relating to how someone can make good decisions and bad decisions.", "B. It is someone’s interest towards various computer technologies.", "C. It is one’s knowledge about various computer technologies, like the different parts to a phone.", "D. It is the technology used for different communications, like telecommunications."],
          ["A. You may inflict harm if someone first inflicted harm to you.", "B. You may not copy or use software that you did not pay for or that you did not receive permission to use.", "C. You should think about the consequences of the program you are writing.", "D. None of the above."]]

mainMenu()