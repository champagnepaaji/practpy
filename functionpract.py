'''
def glassofwater():
    print("Thank you,Please collect your glass of water.")
glassofwater()

def add():
    a=10
    b=20
    c= a+b
    print(c)
add()

def add1(a,b):
    c= a+b
    print(c)
add1(10,45)                             #10,20 are the arguments.

def area_rect(l,b):
    area = l*b
    perimeter=2*(l+b)
    print("The area of the rectangle with length ",l," and width ",b," is ",area," m.sq")
    print("The perimeter of the rectangle with length ",l," and width ",b," is ",perimeter,"m")
num1=int(input("Enter the length of rectangle:"))
num2=int(input("Enter the width of rectangle:"))
area_rect(num1,num2)


def evenodd(x):
    if x %2 == 0:
        print(x,"is an even number.")
    else:
        print(x,"is an odd number.")
num1=int(input("Enter the number you want: "))
evenodd(num1)
def avg(x):
    avg1 = sum(x)/(len(x))
    #print(avg)
    return(avg1)
list1 = [5,6,7,8,9]
# take def avg= sum(a)/len(a)
list2=[10,20,30,40]

print(avg(list1)+avg(list2))
'''

def sq(x):
    num1= x*x
    return(num1)
print(sq(5))

def mult(x,y):
    num2= x*y
    return(num2)
print(mult(10,2)) #a = 2 #b = 7
#(2+7)^2= 2*2 + 7*7+ 2*2*7
print(sq(2)+sq(7)+2*mult(2,7))

def sub(a,b):
    c = a - b
    print(c)
sub(40,30)

def div(a,b):
    c = a/b
    print(c)
div(4,2)

def mult(x,y):
    num2= x*y
    return(num2)
print(mult(10,2)) #a = 2 #b = 7
#(2+7)^2= 2*2 + 7*7+ 2*2*7
print(sq(2)+sq(7)+2*mult(2,7))