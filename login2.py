import tkinter as tk

root=tk.Tk()
l1=tk.Label(root,text="person present")
l1.place(x=0,y=0)

def f1():
    import login1 as lp1
    lp1.abc()

b1=tk.Button(root,text="login page",command=f1)
b1.place(x=100,y=50)
def f2():
        import login1 as lp1
        name = lp1.e1.get()
        l1.configure(text=name)

b2=tk.Button(root,text="Present",command=f2)
b2.place(x=0,y=50)
root.mainloop()
