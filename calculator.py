import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.input_text = tk.StringVar()
        self.scientific_mode = False  # Toggle for scientific mode
        
        self.create_ui()
    
    def create_ui(self):
        self.entry = tk.Entry(self.root, textvariable=self.input_text, font=("Arial", 18), bd=10, relief=tk.GROOVE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8)
        
        self.toggle_button = tk.Button(self.root, text="Scientific", font=("Arial", 12), command=self.toggle_mode)
        self.toggle_button.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        
        self.create_basic_buttons()
    
    def create_basic_buttons(self):
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.destroy()
        
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('C', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('(', 5, 4), (')', 5, 5)
        ]
        
        for (text, row, col) in buttons:
            tk.Button(self.root, text=text, font=("Arial", 14), width=5, height=2,
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)
        
        if self.scientific_mode:
            self.create_scientific_buttons()
    
    def create_scientific_buttons(self):
        sci_buttons = [
            ('sin', 2, 4), ('cos', 3, 4), ('tan', 4, 4), ('log', 5, 4),
            ('sqrt', 2, 5), ('^', 3, 5), ('pi', 4, 5), ('e', 5, 5)
        ]
        
        for (text, row, col) in sci_buttons:
            tk.Button(self.root, text=text, font=("Arial", 14), width=5, height=2,
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)
    
    def toggle_mode(self):
        self.scientific_mode = not self.scientific_mode
        self.create_basic_buttons()
    
    def on_button_click(self, button_text):
        if button_text == "C":
            self.expression = ""
        elif button_text == "=":
            try:
                self.expression = self.expression.replace("^", "**")
                self.expression = self.evaluate_expression()
            except:
                self.expression = "Error"
        else:
            self.expression += button_text
        self.input_text.set(self.expression)
    
    def evaluate_expression(self):
        safe_dict = {"sin": math.sin, "cos": math.cos, "tan": math.tan, 
                     "log": math.log10, "sqrt": math.sqrt, "pi": math.pi, "e": math.e}
        return str(eval(self.expression, {"__builtins__": None}, safe_dict))

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()