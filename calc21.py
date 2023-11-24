import calculator as c

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
        c.add(valuea,valueb)
    elif cs==2:
        c.sub(valuea,valueb)
    elif cs==3:
        c.div(valuea,valueb)
    elif cs==4:
        c.mult(valuea,valueb)
    elif cs==5:
        c.sq(valuea,valueb)
    else:
        print("Enter the valid option.")
