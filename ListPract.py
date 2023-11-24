'''
list1=[10,20,30]                    #  []  Shows that this is list
list2=[10.5,20.5,30.5]
list3=['Raj','Shyaam','Sita']
list4=['a','b','c']
list5=[10,'Raj',10.5,'a']
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print('The second item of list1 is:',list1[1])
a1=(list5[3])
print(a1)
list1.append(40)
print(list1)
list3.append('Vishaal')            # append adds the option to last
print(list3)
list1.insert(2,50)
print(list1)
list3.insert(1,'Jot')
print(list3) 
list1.pop()                          # Pop removes the last option/item
print(list1)                    
list3.pop(2)
print(list3)
list3.remove('Raj')
print(list3)
print(len(list3))
list6 = list1+list2
print(list6)
list7 = list1*3
print(list7)
print(70 in list7)
print(list7[1:6])
list1.sort(reverse=True)                             #Arranges the order           # (reverse=True) for descending
print(list1)
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)
print(sum(list1))
#100 150 and 300
list10=[100,150,300]
list10.append(400)
print(list10)
b1=(sum(list10)/len(list10))                          #Roots of automation len and append
print(b1)
print(min(list1))
print(max(list1))
'''



l1 = [10,20,30]
l2 = ["kinley","Shinley",'Binley']
print(l1[2])
print(l1+l2)
l1.insert(2,40)
l2.insert(2,"Tinley")
print(l1)
print(l2)
l1.append(50)
l2.append("Pinley")
print(l1,l2)
l1.pop(3)
l2.pop(3)
print(l1,l2)
print(l2[1],l1[2])
print(str(l2[1])+str(l1[2]))