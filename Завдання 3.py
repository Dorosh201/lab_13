import tkinter as tk
from math import sin, sqrt

def calculate_function(event=None):
    try:
        x = float(entry_x.get())
        result = 0
        for k in range(1, 13):  # від 1 до 12 включно
            numerator = sin(k * x) + k
            denominator = sqrt(x + 0.1 + 6 * k)
            result += numerator / denominator

        format_result = "{:.4f}".format(result)  
        label_result.config(text="Результат: " + format_result)
    except Exception as e:
        label_result.config(text="Помилка: " + str(e))

root = tk.Tk()
root.title("Обчислення суми")
root.geometry("300x200") 
root.configure(bg='skyblue')

# Зображення
photo = tk.PhotoImage(file="3.png")
label_image = tk.Label(root, image=photo)
label_image.grid(row=0, column=0, columnspan=2, pady=10)

# Написи та поля введення
label_x = tk.Label(root, text="Введіть значення x:")
label_x.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_x = tk.Entry(root)
entry_x.grid(row=1, column=1, padx=10, pady=5)

# Кнопка для обчислення
button_calculate = tk.Button(root, text="Обчислити")
button_calculate.grid(row=2, column=0, columnspan=2, pady=10)
button_calculate.bind('<Button-1>', calculate_function)

# Відображення результату
label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()