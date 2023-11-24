
def add(x,y):
    num = x + y
    return(num)
def mult(x,y):
    num = x*y
    return(num)
def divide(x,y):
    num = x/y
    return(num)
def sub(x,y):
    num = x-y
    return(num)

#prime=int(input("Enter any number: "))
def primen(x):
    for i in range(2,x):
        if x %i==0:
            count='True'
            break
        else:
            count='False'
    if count == 'True':
        print(x,'is not prime.')
    else:
        print(x,'is a prime number')
#primen(prime)
