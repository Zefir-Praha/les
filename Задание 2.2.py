element = list(input("Введите числа включая пробелы : "))
for i in range(1, len(element), 2):
    element[i - 1], element[i] = element[1], element[i - 1]
print(element)