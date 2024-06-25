# Даны температуры за месяц март.
# Необходимо найти количество положительных и отрицательных значений температур в месяце,
# самую низкую и самую высокую температуры,
# а также среднемесячное значение температуры.

temp_march = [10, -3, 5, -2, 7, 14, -1, -5, 12, 16, 0]
plus_temp = sum(1 for temp in temp_march if temp > 0)
minus_temp = sum(1 for temp in temp_march if temp < 0)
print(f'Количество положительных темпепратур: {plus_temp}')
print(f'Количество отрицательных температур: {minus_temp}')

minimal = min(temp_march)
maximal = max(temp_march)
print(f'Самая низкая температура: {minimal}')
print(f'Самая высокая температура: {maximal}')

middle_temp = sum(temp_march)/len(temp_march)
print(f'Средняя температура за месяц: {middle_temp}')