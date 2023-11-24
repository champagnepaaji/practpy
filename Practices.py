'''
for i in range(15,21):
    print('cube of number',i,end=' ')
    print('is',i**3)
    
#write a  program to print square root of every alternate number in the range 1 to 10
for i in range(1,10):
    print(i/0.5,'Square root of number is',i)

# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
# The numbers obtained should be printed in a comma-separated sequence

for i in range(100,401):
    if i%2==0:
        j=i//10
        if j%2==0:
            k=j//10
            if k%2==0:
                print(i,',',end='')
         OR               
#a=10555//10
#print(a)
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
#print( ",".join(items))
for j in items:
    print(j,end=',')

#Write a for loop which appends the square of each number to the new list.

lst1=[3,7,6,8,9,11,15,25]
lst2=[]
for i in lst1:
    lst2.append(i**2)
print(lst2)

#Write a for loop using an if statement, that appends each number to the new list if it's positive.
l1=[111,32,-9,-45,-17,9,85,-10]
l2=[]
for i in l1:
    if i>0:
        l2.append(i)
print(l2)

#WAP to separate positive and negative number from a list.
numb = [23,4,-6,23,-9,21,3,-45,-8]
postive = []
negative = []
for i in numb:
    if i>0:
        postive.append(i)
    else:
        negative.append(i)
print('Positive numbers are:',postive) 
print('Negative numbers are:',negative)

#Write a for loop which appends the type of each element in the first list to the second list
#####################
#Write a program to filter even and odd number from a list.     
x = [10,23,24,35,65,78,90]
even = []
odd = []
for i in x:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("Odd numbers:",odd)        

#Python program to print a multiplication table of a given number                
num = 5
for i in range(11): # (1,11)
    print(num,'x',i,'=',5*i)
#######
# What is Palindrome?
str = "515"
l=len(str) #5
p=l-1
for i in range(p):
    if (str[i]==str[p]):
      #  i=i+1
        p=p-1
        check=True
    else:
        check = False
        print('String is not a palindrome')
        break
if check == True:
    print('String is Palindrome')
'''
#Write a program in Python to reverse a word. <----------------------