"""Lists
Outline:
Write a program to perform the following operations on a List: 1. Create an empty list 2. A list with elements 3. Use * operator 4. Reverse a list

Word Matching
Outline:
Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.

Play with Lists
Outline:
Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements.
Also, find the largest and the smallest number in the list."""

"""empty_list=[]
print()
number=[1,2,3,4,5]
print(number)
triples=[1,2,3] * 3
print(triples)"""
#alist=[100,200,300,400,500]
#mylist=alist[::-1]
#print(mylist,"\n")

"""def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr +=1
            lst.append(word)
    print("list of words with first and last character same\n ",lst)
    return ctr

count=match_words(["dad","mum","xiiix","aba","1221"])
print("number of words having same first and last character same:", count)"""




l =[4,5,1,2,9,7,10,8]
print("orginal list",l)
count=0
for i in l:
    count +=i
avg=count/len(l)
print("sum=",count)
print("average=",avg)
l.sort()
print("smallest element is:",l[0])
print("largest element is:",l[-1])
