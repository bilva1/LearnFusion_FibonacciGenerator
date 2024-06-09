import tkinter as tk
from tkinter import messagebox

def fibonacci_recursive(n):
    """Generate the nth Fibonacci number using a recursive approach."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def generate_fibonacci_sequence(n):
    """Generate the first n Fibonacci numbers using the recursive approach."""
    return [fibonacci_recursive(i) for i in range(n)]

def on_generate():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError("The number must be greater than 0.")
        fib_sequence = generate_fibonacci_sequence(n)
        result_label.config(text=f"Fibonacci sequence for n={n}:\n{fib_sequence}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Setting up the GUI
root = tk.Tk()
root.title("Fibonacci Generator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)
#
label = tk.Label(frame, text="Enter the number of Fibonacci terms:")
label.pack(pady=5)

entry = tk.Entry(frame)
entry.pack(pady=5)


generate_button = tk.Button(frame, text="Generate", command=on_generate,justify="left")
generate_button.pack(pady=5)

result_label = tk.Label(frame, text="", justify="left")
result_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
