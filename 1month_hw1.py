'''Написать программу для вычисления расходов за неделю.
Расход каждого дня недели должен вводиться пользователем по запросу программы (input).
Вывести общую сумму расходов.
Вывести средний расход в день. (средний расход должен быть в дробном числе, округленным с одной цифрой после точки.)

если сумма расходов превысило 20000, вывести на консоль "потрачено много!"
если сумма расходов о 10000 до 20000, вывести на консоль "потрачено средне!
если сумма расходов от 1 до 10000, вывести на консоль "потрачено мало!
в ином случае "не потрачено ничего!"'''



Monday_expense = int(input("Введите расход на понедельник: "))
Tuesday_expense = int(input("Введите расход на вторник: "))
Wednesday_expense = int(input("Введите расход на среду: "))
Thursday_expense = int(input("Введите расход на четверг: "))
Friday_expense = int(input("Введите расход на пятницу: "))
Saturday_expense = int(input("Введите расход на субботу: "))
Sunday_expense = int(input("Введите расход на воскресенье: "))

total_expenses = Monday_expense + Tuesday_expense + Wednesday_expense + Thursday_expense + Friday_expense +\
                 Saturday_expense + Sunday_expense
average_expense = round((total_expenses / 7), 1)

print(f"Общая сумма расходов: {total_expenses}")
print(f"Средний расход в день: {average_expense}")

print("-------------------------------------------------------------")
#lesson2
if total_expenses > 20000:
    print("потрачено много!")
elif total_expenses >= 10000 and total_expenses < 20000:
    print("потрачено средне!")
elif total_expenses >= 1 and total_expenses < 10000:
    print("потрачено мало!")
else:
    print("не потрачено ничего!")

