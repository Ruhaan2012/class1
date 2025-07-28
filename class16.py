"""Tip, the waiter
Outline:
Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant.
Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ),
this function calculates the total amount you should pay.

Cube of the cube
Outline:
Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3

Factorial
Outline:
Write a program to find the factorial using recursive function

def total_cal(bill,tippercent):
    total=bill*(1+0.01*tippercent)
    print("please pay ",total)
total_cal(100,10)



number=int(input("enter the number "))
def cube(number):
    return (number*number*number)
def three(number):
    if number % 3==0:
        print("divisible by 3")
        return cube(number)
    else:
        print("not divisible by 3")
        return cube(number)
print(three(number))


x=int(input("enter the number "))
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
print(fact(x))"""




"""print(fact.__doc__)"""

