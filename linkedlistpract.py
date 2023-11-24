from collections import deque
'''
l1= deque(["a","b","c","d"])          # We dont see the complete list concept :-1 one item is removed other items will cover up. 
print(l1)                                 #first in first out(FIFO) = queue, Last in 1st out (LIFO)= Stacks
l2= deque("abc")
print(l2)
l2.append('d')
print(l2)
l2.appendleft('e')
print(l2)
l2.pop()
print(l2)
l2.popleft()
print(l2)

name1=deque()
while True:
    enter=input("Enter the name to add to the queue OR type r to remove:")
    if enter=='r':
        name1.popleft()
    else :
        name1.append(enter)        
    print(name1)
'''
name1=deque()
while True:
    enter=input('Enter the name to add to the stack OR type r to remove:')
    if enter =='r'or enter =='R':
        name1.popleft()        
    else:
        name1.appendleft(enter)
    print(name1)