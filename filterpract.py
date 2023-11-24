l1 = ["a",'b','c',"d","e",'f',"g"]
def abc(l1):
    vls=['a','e','i','o','u']
    if(l1 in vls):
        return True
    else:
        return (False)
vowels = filter(abc,l1)
print(list(vowels))
