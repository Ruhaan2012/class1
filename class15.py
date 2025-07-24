"""Well wishes
Outline:
Write a program to create a function name well wishes that will give output hello, how are you!

Weather condition
Outline:
Write a program to display the weather in autumn and spring :

Calculator
Outline:
Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide.
Ask for a choice from users which operation they want to perform.
Take user input whatever operation they want to perform And call that function accordingly


def wellwishes():
    print("hello how are you")
wellwishes()

def weather():
    a=input("enter the season(winter or summer) ")
    if a=="winter":
        print("it's very cold here ")
    elif a=="summer":
        print("its very hot here ")
weather()
weather()"""

number=int(input("enter number1 "))
number2=int(input("enter number2 "))
print("please select the operation ")
print("a.addition   b.subtraction    c.multiplication    d.divide    ")
choice=(input("please enter your choice:  "))
def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def divide(p,q):
    return p/q
def multiply(p,q):
    return p*q
if choice=="a":
    print(add(number,number2))
elif choice=="b":
    print(subtract(number,number2))
elif choice=="d":
    print(divide(number,number2))
elif choice=="c":
    print(multiply(number,number2))
else:
    print("invalid input ")

