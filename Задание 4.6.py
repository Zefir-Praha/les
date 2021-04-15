from itertools import count, cycle, islice


def surprise(el1, el2, number):
    try:
        el1, el2, number = int(el1), int(el2), int(number)
        my_list = [el for el in islice(count(), el1, el2 + 1)]
        an_list = iter(el for el in cycle(my_list))
        list_2 = [next(an_list) for _ in range(number)]
        print(my_list)
        return list_2
    except ValueError:
        return "Ошибка"

print(surprise(input("Начало: "), input("Конец: "), input("Повторы: ")))