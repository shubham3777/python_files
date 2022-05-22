import time
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title = ("clock")
 
def time():
    string = strftime('%H:%M:%S %P')
    label.config(text=string)
    label.after(1000,time)

label = Label(root,font=('ds-digital',50), background="black",foreground='cyan')
label.pack(anchor='center')
time()

mainloop()