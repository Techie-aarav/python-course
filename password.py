import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)
    
    if length < 5:
        strength = "Weak"
        color = "red"
    elif length < 8:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"
    
    result_label.config(text=f"Password Strength: {strength}", fg=color)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

# UI Elements
tk.Label(root, text="Enter your password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
