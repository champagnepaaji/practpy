import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")
root["bg"] = "#E2B6AC"
l1=tk.Label(root,text="Enter the First number below :",bg="#FF3A00",font="Times 8 bold italic underline")
l1.place(x=180,y=0)
e1=tk.Entry(root)
e1.place(x=197,y=20)
l2= tk.Label(root,text="Enter the second number below :",bg="#FF3A00",font="Times 8 bold italic underline")
l2.place(x=170,y=40)
e2= tk.Entry(root)
e2.place(x=197,y=60)
l3=tk.Label(root,text="Answer is :",bg="#FF3A00",font="Times 8 bold italic underline")
l3.place(x=225,y=80)
e3= tk.Entry(root)
e3.place(x=197,y=100)
def add1():
    num1=float(e1.get())
    num2=float(e2.get())
    answer= num1+num2
    e3.insert(0,answer) 
b1=tk.Button(root,text="Add",width=6 ,command= add1)
b1.place(x=150,y=140)
def sub1():
    num1=float(e1.get())
    num2=float(e2.get())
    answer= num1-num2
    e3.insert(0,answer) 
b2 = tk.Button(root,text="Subtract",command= sub1)
b2.place(x=210,y=140)
def div1():
    num1=float(e1.get())
    num2=float(e2.get())
    answer= num1/num2
    e3.insert(0,answer)
b3 = tk.Button(root,text="Division",command=div1,bg="#F2D18B",font="Franklin 8 bold ")
b3.place(x=270,y=140)
def mult1():
    num1=float(e1.get())
    num2=float(e2.get())
    answer= num1*num2
    e3.insert(0,answer)
b4 = tk.Button(root,text="Multiply",command= mult1,bg="#F2D18B",font="Franklin 8 bold")
b4.place(x=330,y=140)


root.mainloop()