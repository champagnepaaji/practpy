'''
a = 'Hi there'
i = 0
while (i < 10):
    i=i+1 
    print(i,a) 
    #i = i+1   
print('Thank You')

#table of 7 print with while

p = []
for i in range(1,11): #i=1       
    p.append(i*7) #1*7
    print('7 x',i,'=',p[i-1])
###
for i in range (1,11):
    print('7 x',i,'=',7*i)
'''
'''
while True:                              #IMPORTANT        
    t=int(input('Enter The Table:')) #5                                                     ##main automation
    tyms=int(input('Enter How many times you want the table?:'))
    i=1
    while (i<=tyms): #i=1(true), i=2
        print(t,' x ',i,'=',t*i)
        i=i+1
'''
