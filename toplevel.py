from tkinter import *
root = Tk()
root.geometry("600x700")
root.title("main")
def topwin():
    top = Toplevel()
    top.geometry("700x800")
    top.title("Top level")
    l2 = Label(top , text = "This is top level window")
    l2.pack()
    top.mainloop()
l = Label(root , text = "This is root window ")
btn = Button(root , text = "Click here to open other window" , command = topwin)
l.pack()
btn.pack()
