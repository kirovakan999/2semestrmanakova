# -*- coding: utf8 -*-
#  ПЗ 4 вариант 6 задание 2
# Дано целое число N(>1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 2 + ... + K
# будет меньше или равна N, и саму эту сумму.

def find_largest_K(N):
    K = 0
    total_sum = 0
    while total_sum + (K + 1) <= N:
        K += 1
        total_sum += K
    return K, total_sum

N = 23 # твое целое число N
largest_K, sum_below_N = find_largest_K(N)
print("Наибольшее K:", largest_K)
print("Сумма до K:", sum_below_N)


