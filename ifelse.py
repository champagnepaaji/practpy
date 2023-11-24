#Voting Machine
'''
age=float(input('Enter your age:')) 
#print(age)
if age>=18:
    print('You are eligible to give vote')
elif age<=0:
    print('Enter the correct option')
else:
    print('Wait till you turn 18')
'''
#Traffic Signals
'''
Signal=(input('Enter the colour of traffic Signal(Red/Green/Yellow):'))
if Signal=='Green':
    print('You are good to go')
elif Signal=='Red':
    print('Stop')    
elif Signal=='Yellow':
    print('Watch Carefully')
else:
    print('Enter the correct option')
#Examtable
examd=(input('Enter the Subject:'))
if examd =='Science':
    print('On 14th Sept 2022')
elif examd=='Maths':
    print('On 16th Sept 2022')
elif examd =='English':
    print('On 20th Sept 2022')
elif examd =='CS':
    print('On 22th Sept 2022')
else:
    print('Not a valid subject')

#Number is even or Odd
num1=int(input('Enter the Number:'))
if num1 %2==0:
    print('The Number ',num1,' is even')
else:
    print("The Number ",num1, " is odd")
# Divisible by 5
num1=int(input('Enter the Number:'))
if num1 %5==0:
    print('The number ',num1,' is divisible by 5')
else:
    print('The number ',num1,' not divisible by 5')
#D by 6
num1=int(input('Enter the Number:'))
if num1 %2==0 and num1 %3==0:  #%
    print('The number ',num1,' is divisible by 6')
else:
    print('The number ',num1,' not divisible by 6')

#divisible by 2 or 3 (or)
num1=int(input('Enter the Number:'))
if num1 %2==0 or num1 %3==0:
    print('The number ',num1,' is divisible by 2 or 3')
else:
    print('The number ',num1,' not divisible by 2 or 3')

#List 3 option matches ur input 
l1=['Maths','Chemistry','Physics']
print(l1)
sub=(input('Enter the Subject from Above:'))
if sub == 'Maths':
    print('Solve the equation on integration')
elif sub == 'Chemistry':
    print('Solve the equation on Balancing')
elif sub == 'Physics':
    print('Define Ampere circuital law')
else:
    print('Enter a valid subject')

#
l1=['What is your name?','In which grade do you study?']
l2=['My name is Mannat','I am studying in 12th Grade.']
ques=(input('Enter the question:'))
if ques == l1[0]:
    print(l2[0])
elif ques == l1[1]:
    print(l2[1])
else:
    print('Not a valid question')
#
option_1={'Coffee':1,'Tea':2,'Soup':3}
print(option_1)
choose=(input('What item do you want?'))
if choose == option_1{0}:
    print(option_1{0}
elif choose == option_1
'''
print('option1: Coffee')
print('option2: Tea')
print('option3: Soup')
a=int(input('Select Any one option from above: '))                 
if a == 1:
    print('Your Coffee is Ready!')
elif a == 2:
    print('Your tea is Ready!')
elif a == 3:
    print('Your soup is Ready!')
else:
    print('Enter the valid option')
 
