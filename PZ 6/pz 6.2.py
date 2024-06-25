#Вариант 6
#Дан список размера N. Найти максимальный из его локальных минимумов (локальный минимум - это элемент, который меньше любого из своих соседей).
def find_local_minimums(arr):
    local_minimums = []

    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            local_minimums.append(arr[i])

    return local_minimums

def find_max_local_minimum(arr):
    local_minimums = find_local_minimums(arr)

    if len(local_minimums) == 0:
        return None  # если локальных минимумов нет, вернуть None
    else:
        return max(local_minimums)  # вернуть наибольший из локальных минимумов

# Пример использования
input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = find_max_local_minimum(input_list)
print("Наибольший из локальных минимумов:", result)

