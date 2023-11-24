import tkinter as tk
from tkinter import messagebox

def abc():
    root =tk.Tk()
    global e1
    l1=tk.Label(root,text="user id")
    l1.place(x=0,y=0)
    e1=tk.Entry(root)
    e1.place(x=0,y=40)
    l2=tk.Label(root,text="Password")
    l2.place(x=0,y=80)
    e2=tk.Entry(root,show="*")
    e2.place(x=0,y=120)

    def f2():
        use=e1.get()
        pwd=e2.get()
        if use =="hello" and pwd== "123":
            messagebox.showinfo("Information","Great attendance done")

    b2=tk.Button(root,text="login",command = f2)
    b2.place(x=0,y=160)


    root.mainloop()

