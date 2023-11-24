import array as ar
array1 = ar.array("i",[10,20,30])
print(array1[0])
for i in array1:
    print(i)
array2 = ar.array("d",[10.5,11.5,12.5])
for value in array2:
    print(value)
array1.append(40)
print(array1)
array1.insert(2,25)
print(array1)
array1[2]=27
print(array1)
array3 = ar.array("u","Hi There")
for i in array3:
    print(i)