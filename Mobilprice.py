import class321 as c
print('Select name : Samsung,Nokia')
print("Select Model : S21 , 3310")
name1 = input("Enter the  Name?")
model1 = input("Enter the Model Name?")

if name1.lower()=="samsung"and model1.lower()=="s21":
    c.mobile(name1,model1).display_name()
    c.mobile(name1,model1).model_name()
    print("The price of ",name1,model1,"is",u"\u20b9", "60000")
elif name1.lower()=="Nokia"and model1.lower()=="3310":
    c.mobile(name1,model1).display_name()
    c.mobile(name1,model1).model_name()
    print("The price of",name1,model1,"is",u"\u20b9","3000")
else:
    print("Enter the valid product!")
