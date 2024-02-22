data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')


letters = []
numbers = []

# Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers
for elem in data_tuple:
    if type(elem) == str:
        letters.append(elem)
    else:
        numbers.append(elem)

# Из списка numbers удалить число 6.13 и переместить True в конец списка letters
numbers.remove(6.13)
letters.append(True)

#затем вставить число 2 между 3 и 1
numbers.insert(1, 2)
# Отсортировать numbers, реверсировать letters и изменить пару букв в letters
numbers = sorted(numbers)
letters = letters[::-1]
letters[1] = 'G'
letters[3] = 'e'
letters[7] = 'c'

numbers.remove(1)
numbers = [num**2 for num in numbers]

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)
