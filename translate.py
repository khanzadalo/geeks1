eng = "qwertyuiop[]asdfghjkl;\'zxcvbnm,./"
rus = "йцукенгшщзхъфывапролджэячсмитьбю.,"

word = input("Введите слово: ")

translated_word = ''
for char in word:
    if char.lower() in eng:
        index = eng.index(char.lower())
        translated_word += rus[index]
    elif char.lower() in rus:
        index = rus.index(char.lower())
        translated_word += eng[index]
    else:
        translated_word += char

print("Переведенное слово:", translated_word)