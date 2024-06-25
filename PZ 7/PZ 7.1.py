#Вариант 6
#Дан символ С, изображающий цифру или букву (латинскую или русскую). Если С изображает цифру, то вывести строку «digit», если латинскую букву — вывести строку «lat», если русскую — вывести строку «rus».
def check_character_type(char):
    if char.isdigit():
        return "digit"
    elif char.isalpha() and char.isascii():
        return "lat"
    else:
        return "rus"

# Пример использования
symbol = "Галстян"  # замените на нужный символ
result = check_character_type(symbol)
print(result)
