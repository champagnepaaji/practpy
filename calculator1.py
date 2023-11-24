import class321 as c

print('Option 1: Addition --->')
print('Option 2 : Subtraction -->')
print('Option 3 : Division --->')
print('Option 4 : Multiply --->')
print('Option 5 : Square of Number --->')

while True:
    cs=int(input("What operation you want?Select option from above."))
    valuea = float(input("Enter the value (a) you want to operate::"))
    valueb = float(input("Enter the value (b) you want to operate::"))
    if cs==1:
        answer = c.calc(valuea,valueb)
        answer.add()
    elif cs==2:
        c.calc(valuea,valueb).sub()
    elif cs==3:
        c.calc(valuea,valueb).div()
    elif cs==4:
        c.calc(valuea,valueb).mult()
    else:
        print("Enter the valid option.")


