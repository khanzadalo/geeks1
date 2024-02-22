'''1) Расширить функцию “Ближайшее Число” из ДЗ № 6
На этот раз Функция должна вернуть искомое число и отсортированный список в порядке приближенности к указанному числу.
Всё это должно быть в кортеже. Например:

nearest_number([312, 996, 31, 1991], 1000))
# (1000, [996, 312, 31, 1991])
nearest_number([5, 20.18, 103, 4], 27)
# (27, [20.18, 5, 4, 103])
 '''


def nearest_number(lst, num):
    lst.sort(key=lambda x: abs(x - num))
    return (num, lst)


print(nearest_number([312, 996, 31, 1991], 1000))
print(nearest_number([5, 20.18, 103, 4], 27))

'''2) Создать функцию для вывода элемента списка/кортежа/строки (iterable) по указанному индексу. 
Функция должна работать в бесконечном цикле с командой выхода.
Индекс должен запрашиваться программой при запуске.
При неверно указанном индексе использовать исключения с подсказкой ввода актуальных индексов указанного списка,
например от 0 до последнего индекса.'''


def get_item(iterable):
    while True:
        index = input("Введите индекс элемента (для выхода введите 'q'): ")
        if index == 'q':
            break
        try:
            index = int(index)
            print(iterable[index])
        except ValueError:
            print('Индекс должен быть целым числом')
        except IndexError:
            print(f'Индекс должен быть от 0 до {len(iterable) - 1}')

def get_item(iterable):
    while True:
        index = input("Введите индекс элемента (для выхода введите 'q'): ")
        if index == 'q':
            break
        try:
            index = int(index)
            print(iterable[index])
        except ValueError:
            print("Индекс должен быть целым числом")
        except IndexError:
            print(f"Индекс должен быть от 0 до {len(iterable)-1}")
lst = [1, 5, 6, 7, 10, 12]
get_item(lst)

''' 3) Напишите примеры использования lambda функций с такими функциями как filter, map по одному примеру на своё усмотрение.'''

ten = list(range(1, 11))

# получить только четные числа
filtered_list = list(filter(lambda x: x % 2 == 0, ten))

# возвести в квадрат если число больше или равно 5
map_list = list(map(lambda x: x ** 2 if x >= 5 else x, ten))

print(filtered_list)
print(map_list)
