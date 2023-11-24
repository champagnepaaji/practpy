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
while(i!=6):
    i=int(input("Choose option number you want?:"))
    if (i==1):
        print('Please pay the amount :)')
        amount=int(input('Enter the Amount:'))
        time.sleep(3)
        if (amount>=5):
            balance = (amount-5)
            print("Collect the change $",balance)
            time.sleep(2)
            print('Thank you, Please receive your item from below box :)')
        else:
            balance = (5-amount)
            print("Insufficient amount by $",balance)
    elif (i==2):
        print('Please pay the amount :)')
        time.sleep(3)
        amount=int(input('Enter the Amount:'))
        time.sleep(3)
        if (amount>=5):
            balance = (amount-5)
            print("Collect the change $",balance)
            time.sleep(2)
            print('Thank you, Please receive your item from below box :)')
        else:
            balance = (5-amount)
            print("Insufficient amount by $",balance)
    elif(i==3):
        print('Please pay the amount :)')
        time.sleep(3)
        amount=int(input('Enter the Amount:'))
        time.sleep(3)
        if (amount>=5):
            balance = (amount-5)
            print("Collect the change $",balance)
            time.sleep(2)
            print('Thank you, Please receive your item from below box :)')
        else:
            balance = (5-amount)
            print("Insufficient amount by $",balance)
    elif(i==4):
        print('Please pay the amount :)')
        time.sleep(3)
        amount=int(input('Enter the Amount:'))
        time.sleep(3)
        if (amount>=5):
            balance = (amount-5)
            print("Collect the change $",balance)
            time.sleep(2)
            print('Thank you, Please receive your item from below box :)')
        else:
            balance = (5-amount)
            print("Insufficient amount by $",balance)
    elif(i==5):
        print('Please pay the amount :)')
        time.sleep(3)
        amount=int(input('Enter the Amount:'))
        time.sleep(3)
        if (amount>=5):
            balance = (amount-5)
            print("Collect the change $",balance)
            time.sleep(2)
            print('Thank you, Please receive your item from below box :)')
        else:
            balance = (5-amount)
            print("Insufficient amount by $",balance)  
    time.sleep(3)      
print('Thank You For Using ♥ ')
