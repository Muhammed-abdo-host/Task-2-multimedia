#Muhammed abdo reda abdelgawaad
import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry.pack(fill="x", padx=10, pady=10)

def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get()) 
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", " / ",
    "4", "5", "6", " * ",
    "1", "2", "3", " - ",
    "0", ".", "=", " + "
]

row = 0
col = 0

for btn in buttons:
    if btn == "=":
        tk.Button(frame, text=btn, width=5, height=2, bg="lightgreen",
                  command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(frame, text=btn, width=5, height=2,
                  command=lambda value=btn: button_click(value)).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Clear", bg="red", fg="white",
          font=("Arial", 12), command=clear).pack(fill="x", padx=10, pady=10)

root.mainloop()
