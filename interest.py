import tkinter as tk

def calculate_interest():
    try:
        # Get user inputs
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        # Calculate Simple Interest
        simple_interest = (principal * rate * time) / 100

        # Calculate Compound Interest (compounded annually)
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        # Display Results
        result_label.config(text=f"Simple Interest: {simple_interest:.2f}\n"
                                 f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        result_label.config(text="Invalid Input! Please enter numbers.")

# Create the main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")

# Labels and Entry Fields
tk.Label(root, text="Principal Amount:").pack(pady=5)
principal_entry = tk.Entry(root)
principal_entry.pack(pady=5)

tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)

tk.Label(root, text="Time Period (years):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

# Calculate Button
calculate_btn = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()


