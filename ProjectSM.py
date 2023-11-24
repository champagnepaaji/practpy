supermarket=["Fruits","Vegetables","Books","GeometryBox"]
print(supermarket)
basket=[]
while True:
    Item=input('Select the items from above list:')
    basket.append(Item)
    print("The item you got:",basket)
    print('The number of item you got:',len(basket))
    supermarket.remove(Item)
    print('Item left are :',supermarket)
    print('The number of items left are:',len(supermarket))

    