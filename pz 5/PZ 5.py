# Вариант 6
# Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов python

def display_string_with_length():
    length = input("Введите желаемое количество символов: ")
    while type(length) != int:
        try:
            length = int(length)
        except ValueError:
            print("Вы ввели не цифру!")
            length = input("Введите желаемое количество символов : ")

    output_string = '*' * length  # Создаем строку, содержащую указанное количество звездочек
    print(output_string)  # Выводим строку на экран

# Вызовем функцию
display_string_with_length()
