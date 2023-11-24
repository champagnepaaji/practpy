'''
list1=['maths','science','english']
for i in list1:
    print(i)
    print('Done')
print('Good')
##############
list1=[10,30,40,50]
for i in list1: # i=10 , i=30, i=40, i=50 , loop end,####Reverse Engineering
    print(i)
    print('hi') # hi,hi,hi,hi
print('Good Morning') #Good Morning
#hi
#hi
#hi
#hi
#Good Morning 

for i in range(0,101,1):#i= 0
    print(i)

for i in range(1,101): #i=1,i=2
    #print(i)
    if i %2==0: # 1%2==0 false, 2%2==0 True....,100%2==0 
        print(i,' is Even') #print even....,even
    else:                
        print(i,' is Odd') #print odd,
#1isodd,2iseven....,100iseven

for i in range(1,101,1):
    if i %5==0:
            print(i,' is div by 5') #print even....,even
    else:                
        print(i,' is not div by 5') #print odd

#Write a program to print cubes of numbers in range 15 to 20

for i in range(15,21):
    print(i*i*i,'is the cube of number',i)

#On monday is 21 degree on tuesday is 25, wednesday is 26 , .......
temp=[21,25,26,27,28,29,30]
for i in temp:
    if i==21:
        print('On monday temp is ',i)
    elif i==25:
        print('On tuesday temp is',i)
    elif i==26:
        print('ON wednesday temp is',i)
    elif i==27:
        print('On thursday temp is',i)
    elif i==28:
        print('ON friday temp is',i)
    elif i==29:
        print('ON saturday temp is',i)
    elif i==30:
        print('on sunday temp is',i)

            
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
temp=[21,25,26,27,28,29,30]
for i in range(len(days)):
    print('On',days[i],'Temp is',temp[i])

#Prime numbers  
num1 = 11
for i in range(2,num1):#i=2,i=3,i=4,i
    if num1 %i==0: #num1/2 , num1/3 
        count='True' #true
        break
    else:
        count="False" #false 
if count=="True":
    print(num1,"is not prime.")
else:
    print(num1,"is prime")
'''
'''
num1 = int(input("Enter the number"))
for i in range(2,num1):#i=2,i=3,i=4,i
    if num1 %i==0: #num1/2 , num1/3 
        count='True' #true
        break
    else:
        count="False" #false 
if count=="True":
    print(num1,"is not prime.")
else:
    print(num1,"is prime")
'''
