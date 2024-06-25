import tkinter as tk
from tkinter import ttk


def submit_form():
    # Функция для обработки нажатия на кнопку "REGISTER"
    # Здесь можно добавить код для обработки введенных данных
    pass


# Создание основного окна
root = tk.Tk()
root.title("Event Registration Form")
root.geometry("400x500")

# Заголовок формы
header = tk.Label(root, text="EVENT REGISTRATION FORM", bg="black", fg="white", font=("Arial", 16))
header.pack(fill=tk.X)

# Фрейм для формы
form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(pady=10)

# Поля ввода
labels = ["Name", "Company", "Email", "Phone", "Subject", "Are you an existing customer?"]
fields = {}

for label in labels:
    row = tk.Frame(form_frame)
    row.pack(fill=tk.X, pady=5)

    if label == "Name":
        tk.Label(row, text=label, width=15, anchor='w').pack(side=tk.LEFT)
        fname = tk.Entry(row)
        fname.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X, padx=5)
        lname = tk.Entry(row)
        lname.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        fields[label] = (fname, lname)
    elif label == "Phone":
        tk.Label(row, text=label, width=15, anchor='w').pack(side=tk.LEFT)
        area_code = tk.Entry(row, width=5)
        area_code.pack(side=tk.LEFT, padx=5)
        phone_number = tk.Entry(row)
        phone_number.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        fields[label] = (area_code, phone_number)
    elif label == "Are you an existing customer?":
        tk.Label(row, text=label, width=25, anchor='w').pack(side=tk.LEFT)
        yes_radio = tk.Radiobutton(row, text="Yes", value=1)
        yes_radio.pack(side=tk.LEFT, padx=5)
        no_radio = tk.Radiobutton(row, text="No", value=0)
        no_radio.pack(side=tk.LEFT)
        fields[label] = (yes_radio, no_radio)
    else:
        tk.Label(row, text=label, width=15, anchor='w').pack(side=tk.LEFT)
        entry = tk.Entry(row)
        entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        fields[label] = entry

# Поле выбора темы
row = tk.Frame(form_frame)
row.pack(fill=tk.X, pady=5)
tk.Label(row, text="Subject", width=15, anchor='w').pack(side=tk.LEFT)
subject = ttk.Combobox(row, values=["Option 1", "Option 2", "Option 3"])
subject.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
fields["Subject"] = subject

# Кнопка регистрации
register_button = tk.Button(root, text="REGISTER", bg="red", fg="white", command=submit_form)
register_button.pack(pady=20)

root.mainloop()