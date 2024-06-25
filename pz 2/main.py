# -*- coding: utf8 -*-
# Программа для подсчета полных метров в данном количестве сантиметров

number = input('Введите расстоение (в сантиметрах): ')
try:
    cm = int(number)
    cm = abs(cm)
    if type(cm) == int:
        metre = cm//100
        print(f"{cm} - {metre} полных метров")
    else:
        raise ValueError
except ValueError:
    print('Введите корректное значение.')