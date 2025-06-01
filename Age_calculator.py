import tkinter as tk
from tkinter import ttk


def create_gui():
    # Create main window
    root = tk.Tk()
    root.title("Age Calculator")
    root.geometry("300x150")

    # Configure grid layout
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # Create labels
    ttk.Label(root, text="Birth Year:", font=('Arial', 11)).grid(row=0, column=0, padx=10, pady=10, sticky="we")

    # Create entry fields
    year_entry = ttk.Entry(root, font=('Arial', 11))
    year_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")
    
    age_entry = ttk.Entry(root, font=('Arial', 11), state='readonly')
    age_entry.grid(row=1, column=1, padx=10, pady=10, sticky="we")

    # Submit button
    submit_btn = ttk.Button(root, text="Check Age", command=lambda: submit_data(year_entry, age_entry))
    submit_btn.grid(row=1, column=0, pady=10)

    root.mainloop()

def submit_data(year_entry,age_entry):

    try:
        year = int(year_entry.get())
        if year<2026:
            age = 2025-year
            age_entry.config(state='normal')
            age_entry.delete(0, tk.END)
            age_entry.insert(0, str(age))
            age_entry.config(state='readonly')
            print(age)
        else:
            age_entry.config(state='normal')
            age_entry.delete(0, tk.END)
            age_entry.insert(0,"Future Year!")
            age_entry.config(state='readonly')
    except:
        age_entry.config(state='normal')
        age_entry.delete(0, tk.END)
        age_entry.insert(0,"Invalid entry")
        age_entry.config(state='readonly')

if __name__ == "__main__":
    create_gui()
