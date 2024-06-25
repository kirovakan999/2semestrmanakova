# Вариант 6
# Дана строка-предложение на русском языке. Зашифровать её, выполнив циклическую замену каждой буквы на следующую за ней в алфавите и сохранив при этом регистр букв («А» перейдет в «Б», «а» — в «б», «Б» — в «В», «я» — в «а» и т.д.). Букву «ё» в алфавите не учитывать («е» должна переходить в ‹ок»). Знаки препинания и пробелы не изменять.
def encrypt_russian_sentence(sentence):
    result = ""
    for char in sentence:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if char == 'е':
                new_char = 'ж' if is_upper else 'ж'
            elif char == 'я':
                new_char = 'а' if is_upper else 'а'
            else:
                new_char = chr((ord(char) - ord('а') + 1) % 32 + ord('а')) if is_upper else chr((ord(char) - ord('а') + 1) % 32 + ord('а')).lower()
            result += new_char.upper() if is_upper else new_char
        else:
            result += char
    return result

# Example usage
original_sentence = "Владик в военкомате"
encrypted_result = encrypt_russian_sentence(original_sentence)
print(encrypted_result)
