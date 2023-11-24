import tkinter as tk 
from tkinter import StringVar
def output():
    select ="You choosed "+str(var1.get())
    label1.config(text=select)
    
root= tk.Tk()
root.title("Radio")
root.geometry("500x500")
root["bg"]= "#F2DDB2"
var1=StringVar()
rb1=tk.Radiobutton(root,text="Computer On",variable=var1,value="Turn on the computer.",command=output)
rb1.place(x=0,y=0)
rb2=tk.Radiobutton(root,text="Computer Off",variable=var1,value="Turn off the computer",command=output)
rb2.place(x=110,y=0)
label1=tk.Label(root,text="")
label1.place(x=0,y=50)








root.mainloop()