"""Value Error
Outline:
Write a program to understand how the value error exception works?

Multiple exceptions
Outline:
Write a program to check how the exceptions and finally statement works

Bye Bye
Outline:
Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye."""


"""try :
    num = int(input("enter your number : ")) 
    print(num)
except ValueError as ex:
    print("exception:",ex)


print("i am outside the try block")

try :
    num1=int(input("enter a number: "))
    num2=int(input("enter a number: "))
    result=num1/num2
    print("result is :",result)
    
except ZeroDivisionError:
    print("Division by zero is not allowed ")
except ValueError:
    print("please print numerical value ")
except NameError as ex:
    print("The exception is",ex)

except:
    print("some error occurred ")
finally:
    print("i will execute no matter what happens ")"""



valid=False

while not valid:
    try:
        n= int(input("enter a number: "))
        while n%2 == 0:
            print("bye")
            valid = True

    except ValueError:
        print("invalid")