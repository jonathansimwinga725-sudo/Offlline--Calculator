
import tkinter as tk

# Create the calculator window
root = tk.Tk()
root.title("My Offline Calculator")
root.geometry("340x460")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

expression = ""

display = tk.Entry(
    root,
    font=("Arial", 26),
    bg="#313244",
    fg="white",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=15, pady=20, ipady=18)


def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(0, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def calculate():
    global expression

    try:
        # Only allow basic arithmetic characters
        allowed = "0123456789+-*/.() "
        if not expression or any(
            char not in allowed for char in expression
        ):
            raise ValueError("Invalid expression")

        result = eval(expression, {"__builtins__": {}}, {})
        expression = str(result)

        display.delete(0, tk.END)
        display.insert(0, expression)

    except (ValueError, SyntaxError, ZeroDivisionError,
            TypeError, OverflowError):
        display.delete(0, tk.END)
        display.insert(0, "Error")
        expression = ""


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["(", ")", "="]
]

frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(expand=True, fill="both", padx=15, pady=10)

for row_index, row in enumerate(buttons):
    frame.rowconfigure(row_index, weight=1)

    for col_index, value in enumerate(row):
        frame.columnconfigure(col_index, weight=1)

        if value == "C":
            command = clear
            color = "#f38ba8"
        elif value == "=":
            command = calculate
            color = "#a6e3a1"
        else:
            command = lambda v=value: press(v)
            color = "#45475a"

        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="#11111b" if value in ["C", "="] else "white",
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            padx=4,
            pady=4,
            sticky="nsew"
        )

root.mainloop()
