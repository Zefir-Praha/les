def numbers():
    s = 0
    while True:
        in_list = input("Введите числа для суммирования. Введите 'q' для выхода :").split()
        for number in in_list:
            if number == "q":
                return s
            else:
                try:
                    s += int(number)
                except ValueError:
                    print("Для выхода нажмите 'q'")
        print(f'{s}')


print(numbers())
