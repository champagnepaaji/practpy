import tkinter as tk
from tkinter import messagebox
#import lpg1 as lp1
import subprocess as sp

def f2():
    root["bg"] = "black"
    l1.configure(fg="white",bg = "black")
    l2.configure(fg="white",bg="black")
root = tk.Tk()
#root.wm_attributes("-alpha",0.7)
root.title("Login Page")
root.geometry("500x500")
root["bg"] = "#F2DDB2"

l1= tk.Label(root,text="Username:",bg="#FFFFFF",font="Rockwell 10 bold",fg="black")
l1.place(x=180,y=0)
e1=tk.Entry(root)
e1.place(x=190,y=25)
l2=tk.Label(root,text="Password:",bg="#FFFFFF",font="Rockwell 10 bold", fg="black")
l2.place(x=179,y=48)
e2=tk.Entry(root,show="*")
e2.place(x=190,y=75)
image1 = tk.PhotoImage(file="C:\Python\Daco_6138504.png")
image1=image1.subsample(4)
#image1=image1.phot(1,1,True)
#pic1=tk.Label(root,image=image1, bg="#F2DDB2")
#pic1.place(x=210,y=140) 

def f1():
    username = "champion"
    password = "1234"
    use = e1.get()
    pas = e2.get()


    if use == username and pas == password:
        
        messagebox.showinfo("INFORMATION","Great you have logged in successfully")
        root = tk.Tk()
        ee1=tk.Entry(root)
        ee1.place(x=0,y=0)

        ee1.insert(0,use)
       # lp1.page1()
    else:
        messagebox.showinfo("INFORMATION","Sorry try again!")

b3=tk.Button(root,text="Login",command=f1)
b3.place(x=190,y=100)
b4= tk.Button(root,text="dark theme",command=f2)
b4.place(x=250,y=100)
sp.Popen(["python", r"C:\Python\lpg1.py"])







root.mainloop()
   