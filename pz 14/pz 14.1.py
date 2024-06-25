# Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные адреса»
# перенести в первый файл строки с ненулевыми первым и вторым октетами,
# а во второй – все остальные.
# Посчитать количество полученных строк в каждом файле.

import re
with open('ip_address.txt', 'r') as file:
    lines = file.readlines()[21:]


group1 = []
group2 = []

for line in lines:
    match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    if match:
        octets = match.group().split('.')
        if int(octets[0]) != 0 and int(octets[1]) != 0:
            group1.append(line)
        else:
            group2.append(line)

with open("file_1.txt", 'w') as file1:
    file1.writelines(group1)

with open("file_2.txt", "w") as file2:
    file2.writelines(group2)

count_group1 = len(group1)
count_group2 = len(group2)

print(f'Количество строк в первом файле: {count_group1}')
print(f'Количество строк во втором файле: {count_group2}')