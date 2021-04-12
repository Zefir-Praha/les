def my_func(x, y):
    try:
        x, y = float(x), int(y)
        results = 1
        for _ in range(abs(y)):
            results /= x
        return f'x в степени y: {round (results, 4)}'
    except ValueError:
        return "Только числа"


number_1 = input('введите положительное число, x : ')
number_2 = input('Введите отрицательное число, y : ')
print(my_func(number_1, number_2))