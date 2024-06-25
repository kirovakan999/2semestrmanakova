# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
import random

matrix = [[random.randint(0, 100) for i in range(3)] for row in range(3)]
print('Исходная матрица:')
[print(i) for i in matrix]



def replace(element):
    return 0 if element > 10 else element

new_matrix = [list(map(replace, row)) for row in matrix]

print("\nМатрица с заменой элементов: ")
for row in new_matrix:
    print(row)