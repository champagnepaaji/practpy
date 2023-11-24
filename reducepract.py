from functools import reduce 

def add(a,b):
    return(a+b)
l1= [2,3,5,6]
print(reduce(add,l1))
#2,3,5,6
#5,5,6
#10,6
#16
