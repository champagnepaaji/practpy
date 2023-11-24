str1 = "Sartaaj"
#str11 = []
l=len(str1)  #l=7
p=l-1        #p=6
str111=''    #empty,
for i in range(p+1): #rnge(7) i=0 , i=1 ,i=2,i=3 i=4 i=5 i=6
    str111=str111+str1[p] #new str111= j, new str111= j+a, newstr= j+a+a, newstr=j+a+a+t,newstr=j+a+a+t+r, newstr=j+a+a+t+r+a ,newstr=j+a+a+t+r+a+S
    #str11.append(str1[p])
    p=p-1   #p=5 , p=4 , p=3,p=2,p=1,p=0
#for i in str11:
 #   print(i,end='')
print(str111)    #jaatraS
