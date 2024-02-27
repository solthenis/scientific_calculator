# calculator/calculator.py
import tkinter as tk
from math import sqrt, acos, asin, degrees

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Calculator")
        self.geometry("400x500")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=4, width=14,
                         justify='right')
        entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'acos',
            '0', '.', '=', '+', 'asin',
            'tan', 'cos', 'sin', '(', ')',
            'log', 'exp', 'pi', 'abs', 'clr'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 16), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.result_var.get()

        if button == '=':
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")

        elif button == 'clr':
            self.result_var.set('')

        elif button == 'sqrt':
            try:
                result = str(sqrt(float(current_text)))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")

        elif button == 'pow':
            self.result_var.set(current_text + '**')

        elif button == 'acos':
            try:
                result = str(degrees(acos(float(current_text))))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")

        elif button == 'asin':
            try:
                result = str(degrees(asin(float(current_text))))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")

        else:
            current_text += button
            self.result_var.set(current_text)

def main():
    app = CalculatorApp()
    app.mainloop()

if __name__ == "__main__":
    main()
