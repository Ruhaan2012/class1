"""Break
Outline:
Write a program to check alphabet “A” is present in the given string or not.
And terminate the loop after finding the alphabet “A.”

Pass
Outline:
Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist."
If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.”
If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number.

Continue
Outline:
Write a program to display 1 to 10 numbers in reverse order and skip the number 5.

for i in range (1,10):
    if i==20:
        continue
    print (i)


a=(input("enter the alphabet "))
for i in a:
    if i=="a":
        break
    print(i)

number=int(input("enter the number "))
if number % 20==0:
    print("twist")
elif number % 15==0:
    pass
elif number % 5==0:
    print("fizz")
elif number % 3==0:
    print("buzz")
else:
    print (number)"""

for i in range (10,1,-1):
    if i==5:
        continue
    print (i)