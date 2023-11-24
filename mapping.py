name_length= map(len,["Mannat","Navteg","Gurtej"])
print(list(name_length))
def sq(a):
    answer=a*a
    return(answer)
square = map(sq,[3,4,5]) 
print(list(square))

fruit=["Apples","Bananas","Mangoes","Guavas"]
map_object = map(max,fruit)
print(list(map_object))