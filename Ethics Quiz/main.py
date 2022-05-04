# May 4 2022
# Main 
import time
print("This is a quiz.")

name = input("Please enter you name:\t")
score = 0

print("Thank you! Your name is {}.".format(name))
time.sleep(0.75)

#Question 1
print("Let's begin.")
time.sleep(0.5)

print("Question 1: What is utilitarianism?\n")
print("a. It is the moral philosophy of maximising happiness and minimizing pain.\nb. It is the moral philosophy of thinking that something is good if the intentions are good, rather than the result.\nc. It is the belief that there is only one right way to do something.\nd. It is the belief that only one person should have authority in a given setting.")
quest1 = input("\nType the letter that correspondes to the chosen answer:\t\t")

time.sleep(0.5)

if quest1 == "a." or quest1 == "a":
    print("Correct!")
    time.sleep(0.5)
    score += 1
    print("Score: {}".format(score))
else:
    print("Incorrect.")

time.sleep(0.5)

#Question 2
print("Question 2: What is deontology?\n")
print("a. It is the moral philosophy of thinking optimistically, no matter what situation you are in.\nb.It is the moral philosophy that you should think pessimistically so you do not get hurt by unrealistic expectations.\nc.It is the moral philosophy of believing that the characteristics of an action contribute to if it is good, rather than the result of said action.\nd. It is the belief that you cannot control your life path and that it is chosen for you.\n")
quest2 = input("\nType the letter that correspondes to the chosen answer:\t\t")

time.sleep(0.5)

if quest2 == "c." or quest2 == "c":
    print("Correct!")
    time.sleep(0.5)
    score += 1
    print("Score: {}".format(score))
else:
    print("Incorrect.")

time.sleep(0.5)

