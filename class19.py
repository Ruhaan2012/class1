"""import random as r
import math as m
#print(r.randint(1,50))
#print(r.choice("orange"))
r.seed(1)
print(r.randint(1,30))


Number game
Outline:
Write a program to generate a random integer and match it with the input given by the user?

Rock paper scissors
Outline:
Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer

#Mathematical operations
#Outline:
#Write a program to understand the different functions of the math module.

import random as r
playing = True
number = str(r.randint(10,20))

print("guess a random number between 10 to 20")
print("the game ends when you get 1 hero")
while playing:
    guess=int(input("give me your best guess "))
    if number == guess:
        print("you win the game ")
        print("the number was",number)
        break

    else:
        print("guess again.\n")




import random as r

option = ("rock","paper","scissor")

user=(input("chose rock,paper or scissors: "))

computer=r.choice(option)
print("choose:",user)
print("choose",computer)
if user ==computer:
    print("tie")
elif user == "rock" and computer =="scissor":
    print("you win")
elif user=="paper" and computer == "rock":
    print("you win")
else:
    print("you lose")"""

import math as m
print(m.ceil(4.5))
print(m.floor(4.5))
print(m.factorial(5))
print(m.pow(10,5))
print(m.sqrt(25))
print(m.pi)
print(m.sin(45))