# В матрице элементы первого столбца возвести в куб

import random

matrix = [[random.randint(0, 5) for i in range(3)] for row in range(3)]
print('Исходная матрица:')
[print(i) for i in matrix]

result = map(lambda row: [row[0] ** 3 ] + row[1:], matrix)

print("\nМатрица с заменой элементов: ")
for row in result:
    print(row)