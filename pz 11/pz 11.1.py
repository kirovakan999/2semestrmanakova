# Средствами языка Python сформировать текстовый файл (.txt)
# содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Произведение элементов:
# Повторяющиеся элементы:
# Количество повторяющихся элементов:
# Элементы больше 5 увеличены в два раза:

nums = ['12 44 8 -30 198 -9 8 44 -27']
f1 = open('data_1.txt', 'w')
f1.writelines(nums)
f1.close()

# Исходные данные:
f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(nums)
f2.close()


# Количество элементов:
f1 = open('data_1.txt')
m = f1.read()
m = m.split()
for i in range(len(m)):
    m[i] = int(m[i])
f1.close()

f2 = open('data_2.txt', 'a')
f2.write('\n')
print('Количество элементов: ', len(m), file = f2)
f2.close()


# Произведение элементов
f1 = open('data_1.txt')
multiplier = 1
m = f1.read()
m = m.split()
for i in range(len(m)):
    m[i] = int(m[i])
    multiplier *= m[i]
f1.close()

f2 = open('data_2.txt', 'a')
print('Произведение элементов: ', multiplier, file=f2)
f2.close()


# Повторяющиеся элементы:
f1 = open('data_1.txt', 'r')
nums = list(map(int, f1.read().split()))
duplicates = set()
unique_nums = []
for i in nums:
    if i in unique_nums:
        duplicates.add(i)
    else:
        unique_nums.append(i)
f1.close()

f2 = open('data_2.txt', 'a')
print('Повторяющиеся элементы: ', ' '.join(map(str, duplicates)), file = f2)
f2.close()


# Количество повторяющихся элементов:
f1 = open('data_1.txt', 'r')
nums = list(map(int, f1.read().split()))
f2 = open('data_2.txt', 'a')
for number in set(nums):
    count = nums.count(number)
    if count > 1:
        f2.write(f'Число {number} встречается {count} раз(а)\n')
f2.close()
f1.close()

# Элементы > 5 увеличены в два раза:
f1 = open('data_1.txt', 'r')
nums = list(map(int, f1.read().split()))
proccesed_nums = [num * 2 if num > 5 else num for num in nums]
f2 = open('data_2.txt', 'a')
print("Элементы > 5 увеличены в два раза: ", ' '.join(map(str, proccesed_nums)), file = f2)
f2.close()
f1.close()