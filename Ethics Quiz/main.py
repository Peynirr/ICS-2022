# May 4 2022
# Main

import sys
import time

#Function that prompts the main menu
def mainMenu():
    print("Welcome to the...")
    time.sleep(1)
    #Title
    print(" ___ ____ _____   _____ _   _     _             ___        _     \n|_ _/ ___|_   _| | ____| |_| |__ (_) ___ ___   / _ \ _   _(_)____ \n | | |     | |   |  _| | __| '_ \| |/ __/ __| | | | | | | | |_  / \n | | |___  | |   | |___| |_| | | | | (__\__ \ | |_| | |_| | |/ /\n|___\____| |_|   |_____|\__|_| |_|_|\___|___/  \__\_\___,_|_/___|")
    print("\n")
    print('''888 .d88b .d88b. d88b .d88b. d8      d88b    db     \n 8  8P    YPwww. " dP 8P  Y8  8       wwP   dPYb    \n 8  8b        d8  dP  8b  d8  8 wwww    8  dPwwYb  \n888 `Y88P `Y88P' d888 `Y88P'  8      Y88P dP    Yb ''')
    print("\nBy Group 4.")
    time.sleep(2)

    #Player gets an option to choose from 1-3
    print("")
    print("Please choose an option from 1-3:\t")
    print("[1] Information")
    print("[2] Take the quiz")
    print("[3] Quit")

    selection = int(input("Please enter here:\t"))

    time.sleep(2)
    if selection == 1: #Takes the player to the information fuction
        information()
    elif selection == 2: #Takes the player to the quiz fuction
        newGame()
    elif selection == 3: #Exits out of the game for the player
        exit
    else:
        print("Invalid choice. Enter a number 1-3!") #Takes the player back to the menu to input a correct number
        mainMenu()

#Function that displays the information point by point
def information():
    print(" ___       __                    _   _\n|_ _|_ _  / _|___ _ _ _ __  __ _| |_(_)___ _ _ \n | || ' \|  _/ _ \ '_| '  \/ _` |  _| / _ \ ' \ \n|___|_||_|_| \___/_| |_|_|_\__,_|\__|_\___/_||_|\n")
    time.sleep(1)
    print("\n· Ethics are moral principles that govern a person's behaviour or the conduct of an activity. It’s a philosophy that 'involves systematising, defending, and recommending concepts \nof right and wrong behaviour.' The word ethics originates from the Greek word “ethos”, which means “way of living.” Ethics reflects on human beings and their interactions with the \nenvironment and with other humans. Ethics are very closely related to the independence of individuals, such as making their own choices.\n")
    time.sleep(3)
    print("· Ethical choices are choices that people make because they think they’re right. These choices are made based on values and morals. Many people and businesses have codes of ethics \nso they can make decisions easily.\n")
    time.sleep(3)
    print("· Ethical choices are choices people think are right. The subjective right choices are made based on values and morals.\n")
    time.sleep(3)
    print("· ICT stands for Information and Communications Technology. It is used for communications like management systems, network-based control systems, and telecommunications. \nIt is a broad term referring to anything related to technological communications. ICT ethics relates to how ethics is implemented into computers and technology. This \nsubsection arose mainly due to the issues on the internet. The ten commandments of computer ethics, created by the Computer Ethics Institute,creates a safer environment \non the internet. These rules should be followed by all ICT users. Some examples of these rules are: do not use a computer to harm other people, do not interfere with \nother people’s computer files, do not use a computer to steal, and more.\n")
    time.sleep(3)
    print("· Utilitarianism is an ethical theory that helps make decisions that are based on the outcomes of the event, rather than the motives. With utilitarianism, you can do the \nright thing despite having a bad motive. You also take into account the happiness and interests of everyone rather than being selfish and putting your needs first. An \nexample of utilitarianism is making something free because you know it will help everyone.\n")
    time.sleep(3)
    print("· Deontology is an ethical theory that helps you make decisions based on duty. An action is considered good based on motive, and whether the person had good intentions or \nmorals to begin with, rather than the end result of the action.\n")
    time.sleep(3)
    print("Thank you for reading.\n")
    time.sleep(2)

    playAgain()

def newGame():
    guesses = []
    correctGuesses = 0 #Correct Guesses
    questionNum = 1 #Question number
    print("\n.d88b. 8    8 888 8888P \n8P  Y8 8    8  8    dP  \n8b wd8 8b..d8  8   dP   \n`Y88Pw `Y88P' 888 d8888\n")
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[questionNum - 1]:
            print(i)
        guess = input("Please enter (A, B, C, D):\t")
        time.sleep(1)
        guess = guess.upper()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(key), guess)
        questionNum += 1
    
    displayScore(correctGuesses, guesses)
    playAgain()

#Function to check each answer
def checkAnswer(answer, guess):
    
    if answer == guess: 
        print("You are correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

#Function to display the score at the end of quiz
def displayScore(correctGuesses, guesses):
    print("-------------------------")
    print(" ___ ___ ___ _   _ _  _____ ___ \n| _ \ __/ __| | | | ||_   _/ __| \n|   / _|\__ \ |_| | |__| | \__ \ \n|_|_\___|___/\___/|____|_| |___/\n")
    print("-------------------------")
    
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


#Function to play again
def playAgain():
    response = input("Do you want to go to the main menu?: (Yes or No):\t")
    response = response.upper()

    if response == "YES" or response == "Y":
        mainMenu()
    else:
        bye()

#Function to end the game
def bye():
    print("You are leaving the program...")
    time.sleep(0.5)
    print("Goodbye!")
    exit

#List for the questions along with their answer
questions = {
 "What is utilitarianism?: ": "A", #1
 "What is deontology?: ": "C", #2
 "Moral ethics scenario: Someone hacks your computer to take information with the intent to do harm. You are sad because someone did this as a selfish act without any good intentions. What moral philosophy are they most likely to follow? ": "A", #3
 "What does ICT stand for?: ": "C", #4
 "What is ethics?: ": "B", #5
 "What is a big issue in computer ethics? ": "D", #6
 "What is ICT?: ": "D", #7
 "Which of these are not in the Ten Commandments of Computer Ethics?: ": "A" #8
}

#List for the multiple options for each question
options = [["A. It is the moral philosophy of maximising happiness and minimizing pain.", "B. It is the moral philosophy of thinking that something is good if the intentions are good, rather than the result.", "C. It is the belief that there is only one right way to do something.", "D. It is the belief that only one person should have authority in a given setting."], #1
          ["A. It is the moral philosophy of thinking optimistically, no matter what situation you are in.", "B. It is the moral philosophy that you should think pessimistically so you do not get hurt by unrealistic expectations.", "C. It is the moral philosophy of believing that the characteristics of an action contribute to if it is good, rather than the result of said action.", "D. It is the belief that you cannot control your life path and that it is chosen for you."], #2
          ["A. Utilitarianism", "B. Deontology", "C. None of the above", "D. All of the above"], #3
          ["A. Information and Critical Thinking", "B. Interests towards Computer Technology", "C. Information and Communications Technology", "D. Intellectual Communications Technology"], #4
          ["A. It is ones religion and beliefs about cosmology and something greater than human life.", "B. It is the moral discipline about what is good and what is bad.", "C. It is the steps someone takes to build a proper and successful life.", "D. It is the social skills of an individual and how an individual interacts with others."], #5
          ["A. Internet privacy", "B. Piracy", "C. Harmful actions online", "D. All of the above"], #6
          ["A. It is a thinking skill set relating to how someone can make good decisions and bad decisions.", "B. It is someone’s interest towards various computer technologies.", "C. It is one’s knowledge about various computer technologies, like the different parts to a phone.", "D. It is the technology used for different communications, like telecommunications."], #7
          ["A. You may inflict harm if someone first inflicted harm to you.", "B. You may not copy or use software that you did not pay for or that you did not receive permission to use.", "C. You should think about the consequences of the program you are writing.", "D. None of the above."]] #8

mainMenu()