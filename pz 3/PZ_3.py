# -*- coding: utf8 -*-
# программа для проверки истинности двойного равенства
a = input("Напишите первое число: ")
b = input("Напишите второе число: ")
c = input("Напишите третье число: ")
while type(a) != int:
    try :
        a = int (a)
    except ValueError :
        print("Неправильно ввели!")
        a = input ("Введите первое число : ")

while type(b) != int:
    try :
        b = int (b)
    except ValueError :
        print("Неправильно ввели!")
        b = input("Введите второе число: ")

while type(c) != int:
    try :
        c= int (c)
    except ValueError :
        print("Неправильно ввели!")
        с = input("Введите третье число: ")


if a == b and b == c:
    print("Справедливо двойное равенство")
else:
    print("Двойное равенство не справедливо")
