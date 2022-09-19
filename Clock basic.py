import time
from tkinter import *

root = Tk()

root.geometry("359x150+0+0")

root.configure(background="black")
root.resizable(0,0)

root.overrideredirect(1)

def start():
    text = time.strftime("%H:%M:%S")
    label.configure(text=text)
    label.after(200,start)

label = Label(root,font=("ds-digital",50,"bold"),bg='black',fg='red',bd=50)
label.grid(row=0,column=1)
start()
print("Clock")
root.mainloop()