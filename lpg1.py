import tkinter as tk

#import loginpage as lp
def page1():
        def ff1():
                import logindata as ld

                name = ld.ee1.get()
                l4.configure(text=name)
                    
        root1=tk.Tk()        
        root1.title("Attendance")
        root1.geometry("500x500")
        root1["bg"] = "#F2DDB2"
        l3 = tk.Label(root1,text="Attendence",bg="#FFFFFF",font="Rockwell 10 bold")
        l3.place(x=50,y=0)
        l4 = tk.Label(root1,text="Person Login")
        l4.place(x=50,y=100)
        b2= tk.Button(root1,text="Present",command=ff1)
        b2.place(x=50,y=50)
        root1.mainloop()