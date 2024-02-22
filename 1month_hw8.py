'''Написать программу, которая должна:

1)Прочитать данные из файла results.txt
2)Создать словарь, где ключом будет имя, а значением оценка.
3)Отсортировать словарь по значению в убывающем порядке.
4)Вывести на экран топ-3 лучших студента по оценке.
5)Вывести на экран среднюю оценку.
6)Создать новый текстовый файл sorted_results.txt на основе отсортированного словаря.'''

#1
with open('results.txt', 'r') as f:
    data = f.readlines()

#2
results = {}
for i, line in enumerate(data):
    if i < 2:
        continue  # Пропустить первые две строки в файле
    name, score = line.strip().split()
    results[name] = int(score)

# 3
sorted_results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}

# 4
top_three = list(sorted_results.items())[:3]
print('Top-3 студента:\n----------------')
for student in top_three:
    print(f'{student[0]}: {student[1]}')

# 5
mean_score = sum(results.values()) / len(results)
print(f'\nСредняя оценка: {mean_score}')

# 6
with open('sorted_results.txt', 'w') as f:
    for name, score in sorted_results.items():
        f.write(f'{name} {score}\n')



