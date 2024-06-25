import tkinter as tk
from tkinter import ttk

def calculate_meters():
    cm = int(entry_distance.get())
    meters = cm // 100
    label_result.config(text=f"Полных метров: {meters}")

root = tk.Tk()
root.title("Конвертер сантиметров в метры")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, padx=10, pady=10)

label_distance = ttk.Label(frame, text="Введите расстояние в сантиметрах:")
label_distance.grid(row=0, column=0, padx=5, pady=5)

entry_distance = ttk.Entry(frame)
entry_distance.grid(row=0, column=1, padx=5, pady=5)

button_calculate = ttk.Button(frame, text="Вычислить", command=calculate_meters)
button_calculate.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

label_result = ttk.Label(frame, text="")
label_result.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()