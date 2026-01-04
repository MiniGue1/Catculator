import tkinter as tk
from tkinter import font
import ast
import operator as op

ASCII_CAT = r"""
  /\_/\
 ( o.o )
  > ^ <
  I dunno
"""

# Safe eval implementation (supports + - * / % **, unary +/-, parentheses)
operators = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv,
    ast.Pow: op.pow, ast.Mod: op.mod, ast.UAdd: op.pos, ast.USub: op.neg
}

def _safe_eval_node(node):
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
    if isinstance(node, ast.Num):  # older Python versions
        return node.n
    if isinstance(node, ast.BinOp):
        left = _safe_eval_node(node.left)
        right = _safe_eval_node(node.right)
        op_type = type(node.op)
        if op_type in operators:
            return operators[op_type](left, right)
    if isinstance(node, ast.UnaryOp):
        operand = _safe_eval_node(node.operand)
        op_type = type(node.op)
        if op_type in operators:
            return operators[op_type](operand)
    raise ValueError("Unsupported expression")

def safe_eval(expr):
    node = ast.parse(expr, mode='eval')
    return _safe_eval_node(node.body)

class FakeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(bg="#2b2b2b")

        self.display_var = tk.StringVar()
        self._create_widgets()
        self._bind_keys()

    def _create_widgets(self):
        # Display
        disp_font = font.Font(family="Segoe UI", size=20, weight="bold")
        entry = tk.Entry(self, textvariable=self.display_var, font=disp_font, bd=0, bg="#1e1e1e", fg="#ffffff", justify='right')
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)
        entry.focus()

        btn_cfg = dict(width=4, height=2, bd=0, bg="#333333", fg="#fff", activebackground="#444", activeforeground="#fff")
        btn_font = font.Font(size=14)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('C', 5, 2), ('%', 5, 3),
        ]

        for (text, r, c) in buttons:
            action = (lambda t=text: self._on_button(t))
            b = tk.Button(self, text=text, font=btn_font, command=action, **btn_cfg)
            b.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")

        # Make grid expand nicely
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def _bind_keys(self):
        for ch in '0123456789.+-*/()%':
            self.bind(ch, lambda e, ch=ch: self._insert(ch))
        self.bind('<Return>', lambda e: self._on_equal())
        self.bind('=', lambda e: self._on_equal())
        self.bind('<BackSpace>', lambda e: self._backspace())
        self.bind('c', lambda e: self._clear())
        self.bind('C', lambda e: self._clear())

    def _insert(self, ch):
        self.display_var.set(self.display_var.get() + ch)

    def _on_button(self, label):
        if label == '=':
            self._on_equal()
        elif label == 'C':
            self._clear()
        else:
            self._insert(label)

    def _backspace(self):
        self.display_var.set(self.display_var.get()[:-1])

    def _clear(self):
        self.display_var.set("")

    def _on_equal(self):
        # Always show the ASCII cat when '=' is pressed
        self._show_cat()

    def _show_cat(self):
        cat_win = tk.Toplevel(self)
        cat_win.title("Surprise!")
        cat_win.resizable(False, False)
        cat_win.configure(bg="#222")

        mono = font.Font(family="Courier", size=18)
        lbl = tk.Label(cat_win, text=ASCII_CAT, font=mono, bg="#222", fg="#fff", justify='center')
        lbl.pack(padx=20, pady=20)

        btn = tk.Button(cat_win, text="Close", command=cat_win.destroy, bg="#555", fg="#fff", bd=0, padx=10, pady=5)
        btn.pack(pady=(0, 16))

        # Center the cat window over the main window
        self.update_idletasks()
        x = self.winfo_rootx() + (self.winfo_width() // 2) - (cat_win.winfo_reqwidth() // 2)
        y = self.winfo_rooty() + (self.winfo_height() // 2) - (cat_win.winfo_reqheight() // 2)
        cat_win.geometry(f'+{x}+{y}')

if __name__ == '__main__':
    app = FakeCalculator()
    app.mainloop()
