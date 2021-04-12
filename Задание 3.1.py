def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        num = s_1 / s_2
    except ValueError:
        return "Ошибка"
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    return round(num, 2)
print(div(input("Введите первое число: "), input("Введите второе число: ")))