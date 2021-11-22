from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("Clock")
def time():
    string=strftime('%H:%M:%S %p')
    Label.config(text=string)
    Label.after(1000,time)
Label=Label(root,font=("Algerian",80),background="black",foreground="blue")
Label.pack(anchor="center")
time()
root.mainloop()
