import numpy as np
import tkinter as tk
from tkinter import messagebox

# ---------- Functions ----------
def get_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except:
        raise ValueError("Please enter the matrix in correct format.")

def show_result(result):
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)
    result_box.config(state="disabled")

def add():
    try:
        A = get_matrix(matrix_a.get("1.0", tk.END))
        B = get_matrix(matrix_b.get("1.0", tk.END))
        show_result(A + B)
    except Exception as e:
        messagebox.showerror("Error", e)

def subtract():
    try:
        A = get_matrix(matrix_a.get("1.0", tk.END))
        B = get_matrix(matrix_b.get("1.0", tk.END))
        show_result(A - B)
    except Exception as e:
        messagebox.showerror("Error", e)

def multiply():
    try:
        A = get_matrix(matrix_a.get("1.0", tk.END))
        B = get_matrix(matrix_b.get("1.0", tk.END))
        show_result(np.dot(A, B))
    except Exception as e:
        messagebox.showerror("Error", e)

def transpose():
    try:
        A = get_matrix(matrix_a.get("1.0", tk.END))
        show_result(A.T)
    except Exception as e:
        messagebox.showerror("Error", e)

def determinant():
    try:
        A = get_matrix(matrix_a.get("1.0", tk.END))
        det = np.linalg.det(A)
        show_result(f"Determinant = {det:.2f}")
    except Exception as e:
        messagebox.showerror("Error", e)

# ---------- GUI Window ----------
root = tk.Tk()
root.title("Matrix Operations Tool")
root.geometry("720x600")
root.config(bg="#f4f6f8")

title = tk.Label(
    root,
    text="Matrix Operations Tool",
    font=("Segoe UI", 20, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50"
)
title.pack(pady=10)

# ---------- Input Frame ----------
input_frame = tk.Frame(root, bg="#f4f6f8")
input_frame.pack(pady=10)

# Matrix A
tk.Label(
    input_frame,
    text="Matrix A",
    font=("Segoe UI", 12, "bold"),
    bg="#f4f6f8"
).grid(row=0, column=0, padx=20)

matrix_a = tk.Text(input_frame, height=6, width=30, font=("Consolas", 11))
matrix_a.grid(row=1, column=0, padx=20)

# Matrix B
tk.Label(
    input_frame,
    text="Matrix B",
    font=("Segoe UI", 12, "bold"),
    bg="#f4f6f8"
).grid(row=0, column=1, padx=20)

matrix_b = tk.Text(input_frame, height=6, width=30, font=("Consolas", 11))
matrix_b.grid(row=1, column=1, padx=20)

# ---------- Buttons ----------
button_frame = tk.Frame(root, bg="#f4f6f8")
button_frame.pack(pady=15)

btn_style = {
    "font": ("Segoe UI", 11, "bold"),
    "bg": "#3498db",
    "fg": "white",
    "width": 14,
    "bd": 0,
    "padx": 5,
    "pady": 5
}

tk.Button(button_frame, text="Add", command=add, **btn_style).grid(row=0, column=0, padx=8, pady=5)
tk.Button(button_frame, text="Subtract", command=subtract, **btn_style).grid(row=0, column=1, padx=8, pady=5)
tk.Button(button_frame, text="Multiply", command=multiply, **btn_style).grid(row=0, column=2, padx=8, pady=5)

tk.Button(button_frame, text="Transpose A", command=transpose, **btn_style).grid(row=1, column=0, padx=8, pady=5)
tk.Button(button_frame, text="Determinant A", command=determinant, **btn_style).grid(row=1, column=1, padx=8, pady=5)

# ---------- Result ----------
tk.Label(
    root,
    text="Result",
    font=("Segoe UI", 14, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50"
).pack(pady=5)

result_box = tk.Text(
    root,
    height=6,
    width=65,
    font=("Consolas", 12),
    state="disabled",
    bg="#ecf0f1"
)
result_box.pack(pady=5)

# ---------- Footer ----------
footer = tk.Label(
    root,
    text="Enter matrices row-wise (space separated)",
    font=("Segoe UI", 10),
    bg="#f4f6f8",
    fg="#7f8c8d"
)
footer.pack(pady=10)

root.mainloop()
