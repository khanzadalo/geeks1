vowels = "aeiouаеёиоуыэюя"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзклмнпрстфхцчшщъыьэю"
vowels_count = 0
consonants_count = 0

while True:
    word = input("Введите слово: ")
    if word == 'exit':
      print('Выход')
      break

    for letter in word:
      if letter.lower() in vowels:
        vowels_count += 1
      elif letter.lower() in consonants:
        consonants_count += 1
    
    total_volves = vowels_count + consonants_count
    
    vowel_percent = round((vowels_count / total_volves) * 100, 2)
    consonant_percent = round((consonants_count / total_volves) * 100, 2)
    
    print("Количество букв:", total_volves)
    print("Согласных букв:", consonants_count)
    print("Гласных букв:", vowels_count)
    print("Согласные/Гласные: {}%/ {}%".format(consonant_percent, vowel_percent))
    
    if vowels_count + consonants_count > 0:
      ratio = consonants_count / (vowels_count + consonants_count) * 100
      print(f"Согласные/Гласные: {ratio:.2f}% / {(100 - ratio):.2f}%")