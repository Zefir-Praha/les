number = [8, 8, 8, 5, 5, 4, 3, 2, 1]
user_num = int(input('Введите целое число от 0 до 9: '))
i = 0
for n in number:
    if user_num <= n:
        i += 1
number.insert(i, user_num)
print(number)