# 0107-10271-24 | Reagan II S. Sotelo | BSCS - 1A
# Last Modified: 15/04/2025 | 1:20 AM

import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        # Initialize the main window properties
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("500x250")
        self.root.resizable(False, False)

        # Dictionary mapping operation names to corresponding methods
        self.operations = {
            "Add": self.add,
            "Subtract": self.subtract,
            "Multiply": self.multiply,
            "Divide": self.divide
        }

        # Validation command for numeric input
        self.vcmd = (self.root.register(self.is_valid_number), "%P")

        self.setup_ui() # Setup the UI elements

    # Operation methods
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y): return x / y if y != 0 else "Error: Div by 0"

    # Check if input is a valid float or empty (allows deletion)
    def is_valid_number(self, value):
        if value == "":
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

    # Resets entry fields and result label
    def clear_entries(self):
        for entry in (self.entry_x, self.entry_y):
            entry.delete(0, 'end')
            entry.insert(0, "0")
        self.label_result.config(text="Result: ")

    # Handles button press, performs the selected operation
    def on_button_click(self, operation):
        try:
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())
            result = self.operations[operation](x, y)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.label_result.config(text=f"Result: {result}")
        except ZeroDivisionError:
            self.label_result.config(text="Error: Cannot divide by zero.")
        except ValueError:
            self.label_result.config(text="Error: Invalid number input.")

    # Builds the layout and interface
    def setup_ui(self):
        # Entry fields with 0 placeholder logic on focus
        self.entry_x = tk.Entry(self.root, validate="key", validatecommand=self.vcmd,
                                font=("Arial", 24), bg="#bebebe", fg="black", justify="left")
        self.entry_x.pack(fill="x", ipady=5)
        self.entry_x.insert(0, "0")
        self.entry_x.bind("<FocusIn>", lambda e: self.on_focus_in(self.entry_x))
        self.entry_x.bind("<FocusOut>", lambda e: self.on_focus_out(self.entry_x))

        self.entry_y = tk.Entry(self.root, validate="key", validatecommand=self.vcmd,
                                font=("Arial", 24), bg="#bebebe", fg="black", justify="left")
        self.entry_y.pack(fill="x", ipady=5)
        self.entry_y.insert(0, "0")
        self.entry_y.bind("<FocusIn>", lambda e: self.on_focus_in(self.entry_y))
        self.entry_y.bind("<FocusOut>", lambda e: self.on_focus_out(self.entry_y))

        # Operation buttons and layout
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="both", expand=True)

        for i, label in enumerate(self.operations):
            btn = tk.Button(button_frame, text=label, font=("Tahoma", 12),
                            command=lambda op=label: self.on_button_click(op))
            btn.grid(row=0, column=i, sticky="nsew", padx=2, pady=2)
            button_frame.grid_columnconfigure(i, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)

        # Clear button spanning the width of the button row
        clear_btn = tk.Button(button_frame, text="Clear", font=("Tahoma", 12),
                              command=self.clear_entries)
        clear_btn.grid(row=1, column=0, columnspan=len(self.operations),
                       sticky="nsew", padx=2, pady=2)

        # Result display label
        self.label_result = tk.Label(self.root, text='Result: ', font=("Arial", 18),
                                     bg="#bebebe", fg="black")
        self.label_result.pack(pady=10, ipadx=30, fill="x")

    # Clear placeholder on focus
    def on_focus_in(self, entry):
        if entry.get() == "0":
            entry.delete(0, "end")

    # Restore placeholder on focus out if empty
    def on_focus_out(self, entry):
        if entry.get().strip() == "":
            entry.insert(0, "0")

# Starts the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()