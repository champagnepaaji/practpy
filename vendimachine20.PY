import time
i=0
print("================================================")
print("==========>> Mannat's Vending Machine <<==========")
print("================================================")
print("1. Coke",'5$')
print("2. Fanta",'5$')
print("3. Limca",'5$')
print("4. Chips",'8$')
print("5. Lime Soda",'2$')
print("6. Exit")
def r1(price,item):
    print('Please pay the amount :)')
    amount=int(input('Enter the Amount:'))
    time.sleep(3)
    if (amount>=price):
        balance = (amount-price)
        print("Collect the change $",balance)
        time.sleep(2)
        print('Thank you, Please receive your',item,'from below box :)')
    else:
        balance = (price-amount)
        print("Insufficient amount by $",balance)
while(i!=6):
    i=int(input("Choose option number you want?:"))
    if (i==1):
     r1(5,'coke')    
    elif (i==2):
     r1(5,'Fanta')                   
    elif(i==3):
     r1(5,'Limca')       
    elif(i==4):
     r1(8,'Chips')
    elif(i==5):
     r1(2,'Lime Soda')  
    time.sleep(3)      
print('Thank You For Using ♥ ')
