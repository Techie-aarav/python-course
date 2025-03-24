from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
def msg():
    messagebox.askquestion("Question box", "Do you want to continue to order?")
button = Button(root , text = "Click here to order the food" , command = msg)
button.place(x = 40 , y = 80)
root.mainloop()