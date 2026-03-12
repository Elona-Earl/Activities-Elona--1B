import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("275x200")
window.resizable(True, True)

result_label = tk.Label(window, text="Please enter 2 numbers and choose operators", font=("Arial",10))
result_label.pack()

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    add = num1 + num2
    result_label.config(text=f"The sum is of {num1} + {num2} is {add}.")

def subtract():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    subtract = num1 - num2
    result_label.config(text=f"The difference of {num1} - {num2} is {subtract}.")

def multiply():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    multiply = num1 * num2
    result_label.config(text=f"The product of {num1} x {num2} is {multiply}.")

def divide():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    if num2 == 0:
        result_label.config(text="Cannot divide by zero.")
    else:
        divide = num1 / num2
        result_label.config(text=f"The division of {num1} ÷ {num2} is {divide}.")

frame = tk.Frame(window, bg="lightblue", padx=10, pady=10)
frame.pack(fill="both", expand=True)

label1 = tk.Label(frame, text="Enter 1st Number:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(frame, text="Enter 2nd Number:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(frame, text="Add", width=10, command=add)
btn_add.grid(row=2, column=0, pady=5)

btn_sub = tk.Button(frame, text="Subtract", width=10, command=subtract)
btn_sub.grid(row=2, column=1, pady=5)

btn_mul = tk.Button(frame, text="Multiply", width=10, command=multiply)
btn_mul.grid(row=3, column=0, pady=5)

btn_div = tk.Button(frame, text="Divide", width=10, command=divide)
btn_div.grid(row=3, column=1)

window.mainloop()