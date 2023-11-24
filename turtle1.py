import turtle as t
t.shape("turtle")
t.shapesize(5)
t.fillcolor("blue")
t.speed("fastest")
t.pencolor("green")
t.pensize(1)
'''
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
#####
i=0
while(i<4):
    t.forward(200)
    t.left(90)
    i=i+1

i=0
while(i<4):
    t.forward(200)
    t.left(90)
    i=i+1
t.right(90)
t.forward(200)


i=0
while(i<5):
    t.forward(200)
    t.left(72)
    i=i+1

i=0
length=200
colors = ["red","blue","orange","green","yellow"]
while(i<200):
    t.pencolor(colors[i%5])
    t.forward(length)
    t.left(150)
    i=i+1
    length=length-2
'''
i=0
length=50
colors = ["red","blue","orange","green","yellow"]
while(i<200):
    t.pencolor(colors[i%5])
    t.circle(length)
    t.left(2)
    i=i+1
    #length=length-2


t.mainloop()