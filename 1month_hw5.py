data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

for item in data:
    if item.isdigit():
        codes.append(item)
    else:
        designations.append(item)

print(designations)
print(codes)


operators = {}
i = 0
while i < len(designations):
    operator_name = designations[i]
    operator_code = codes[i]

    if operator_name not in operators:
        operators[operator_name] = set()
        operators[operator_name].add(operator_code)
    i += 1

print(operators)


# Удалить нефункционирующие операторы из словаря operators. (Katel, Fonex)
del operators["Katel"]
del operators["Fonex"]



# Добавить/Обновить к уже существующим номерам (Ошке, Меге и Билайну) пару кодов содержащихся в множестве.
operators["O!"].update(["0700", "0500"])
operators["Megacom"].update(["0999", "0555"])
operators["Beeline"].update(["0222", "0777"])
print(operators)

#В итоге вывести на экран наименования операторов и соответствующие номера в таком виде (в паре ключ-значение)
print("O! -", operators["O!"])
print("Megacom -", operators["Megacom"])
print("Beeline -", operators["Beeline"])
