'''Написать функцию “Чётное-Нечётное”
У функции должен быть один обязательный параметр - целое число.
Функция должна вернуть True, если переданный аргумент чётное число или False, если нечётное.
Если переданный аргумент не является целым числом, вернуть None.'''

def is_even(num):
    if not isinstance(num, int):
        return None
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(123))


''' Написать функцию “Правописание”.
Функция должна принимать предложение, затем возвращать True, если оно начинается с заглавной буквы и 
заканчивается точкой. В противном случае вернуть False.'''

def spelling(sentence):
    if sentence[0].isupper() and sentence[-1] == '.':
        return True
    else:
        return False
print(spelling('Hello, world.'))


'''Написать функцию “Калькулятор”
 У функции должно быть три обязательных позиционных аргумента:   число 1, оператор и число 2.
Калькулятор должен работать по всем арифметическим операторам в Python`е.
В итоге функция возвращает результат, например:
calculator(2, ‘**’, 3) == 8
calculator(5, ‘+’, 9.6) == 14.6
calculator(20, ‘%’, 3) == 2'''

def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '//':
        return num1 // num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2
    else:
        return 'Invalid operator'

print(calculator(5, '+', 9.6))
print(calculator(18, '-', 8))
print(calculator(20, '*', 3))
print(calculator(28, '/', 4))
print(calculator(2, '**', 5))
print(calculator(20, '%', 3))
print(calculator(30, '//', 8))

'''Написать функцию “Ближайшее Число”.
Функция должна принимать два аргумента: 
1) список или кортеж - состоящий из целых или дробных чисел (обязательный параметр)
2) целое или дробное число (параметр по умолчанию = 0)
Функция должна вернуть число из последовательности, которое ближе всего к указанному. Например:
[5, 20.18, 103, 4], 27 == 20.18
(312, 996, 31, 1991), 1000 == 996
Функция принимает список с числами, и одно число, затем возвращает ближайшее число из списка к указанному.'''

def closest_number(numbers, target=0):
    closest_num = numbers[0]
    for num in numbers:
        if abs(num - target) < abs(closest_num - target):
            closest_num = num
    return closest_num

print(closest_number([5, 20.18, 103, 4], 27))
print(closest_number((312, 996, 31, 1991), 1000))
