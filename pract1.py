'''
#factorial of 5!
num1=5
sum=0
# facto=1
for i in range(1,num1+1):#i=1, i=2, i=3 i=4 i=5
    sum=sum+i
   # facto=facto*i #facto=1*1=1, 1*2=2 2*3=6 6*4=24,24*5= 120
print(sum)
#print(facto) #120

     

import classpractice as cp

cp.area (10,20,3).rectangle()
a1 = cp.area(0,0,5)
a1.circle()
'''

import unitconverter as uc
uc.uc(500).cm_to_inches()
u1= uc.uc(500)
u1.cm_to_inches()
u1.cm_to_m()
u1.m_to_cm()