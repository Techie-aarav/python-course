import tkinter as tk
from tkinter import messagebox
from datetime import datetime
def calculate_age():
    dob = entry.get()
    try:
        dob_date = datetime.strptime(dob, "%d-%m-%Y")
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        messagebox.showinfo("Age Calculator", f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter the date in DD-MM-YYYY format")
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")
tk.Label(root, text="Enter your Date of Birth (DD-MM-YYYY):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)
root.mainloop()
