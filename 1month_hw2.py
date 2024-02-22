counter = 5
while counter > 0:
    day = int(input("Введите день рождения (число от 1 до 31): "))
    month = int(input("Введите месяц рождения (число от 1 до 12): "))

    if (day > 31 or day < 1) or (month > 12 or month < 1):
        print("Недействительная дата")
        continue
    elif(21 <= day <= 31 and month == 1) or (1 <= day <= 18 and month == 2):
        print("Водолей!")
    elif (19 <= day <= 29 and month == 2) or (1 <= day <= 20 and month == 3):
        print("Рыбы!")
    elif (21 <= day <= 31 and month == 3) or (1 <= day <= 19 and month == 4):
        print("Овен!")
    elif (20 <= day <= 30 and month == 4) or (1 <= day <= 20 and month == 5):
        print("Телец!")
    elif (21 <= day <= 31 and month == 5) or (1 <= day <= 21 and month == 6):
        print("Близнецы!")
    elif (22 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
        print("Рак!")
    elif (23 <= day <= 31 and month == 7) or (1 <= day <= 22 and month == 8):
        print("Лев!")
    elif (23 <= day <= 30 and month == 8) or (1 <= day <= 22 and month == 9):
        print("Дева!")
    elif (23 <= day <= 30 and month == 9) or (1 <= day <= 23 and month == 10):
        print("Весы!")
    elif (24 <= day <= 31 and month == 10) or (1 <= day <= 22 and month == 11):
        print("Скорпион!")
    elif (23 <= day <= 30 and month == 11) or (1 <= day <= 21 and month == 12):
        print("Стрелец!")
    elif (22 <= day <= 31 and month == 12) or (1 <= day <= 20 and month == 1):
        print("Козерог!")
        
    counter -= 1
    if counter == 0:
        break