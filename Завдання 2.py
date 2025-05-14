import tkinter as tk
from math import sqrt

def calculate_geometry(event=None):
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    # Півпериметр
    p = (a + b + c) / 2

    # Площа за формулою Герона
    S = sqrt(p * (p - a) * (p - b) * (p - c))

    # Радіус вписаного кола
    r = S / p

    # Бісектриса до сторони a
    l_a = sqrt(b * c * (1 - (a ** 2) / ((b + c) ** 2)))

    # Виведення результатів
    result_text = f"Радіус вписаного кола: {r:.3f}\nБісектриса до сторони a: {l_a:.3f}"
    label_result.config(text=result_text)

root = tk.Tk()
root.title("Геометричні розрахунки")
root.geometry("300x200")
root.configure(bg='lightblue')

photo = tk.PhotoImage(file=r"2.png")
label_image = tk.Label(root, image=photo, bg='lightblue')
label_image.grid(row=0, column=0, columnspan=2, pady=10)

# Поля введення
label_a = tk.Label(root, text="Сторона a:", bg='lightblue')
label_a.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1, padx=10, pady=5)

label_b = tk.Label(root, text="Сторона b:", bg='lightblue')
label_b.grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1, padx=10, pady=5)

label_c = tk.Label(root, text="Сторона c:", bg='lightblue')
label_c.grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=3, column=1, padx=10, pady=5)

# Кнопка обчислення
button_calc = tk.Button(root, text="Обчислити")
button_calc.grid(row=4, column=0, columnspan=2, pady=10)
button_calc.bind('<Button-1>', calculate_geometry)

# Виведення результату
label_result = tk.Label(root, text="", bg='lightblue', font=("Arial", 12))
label_result.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()