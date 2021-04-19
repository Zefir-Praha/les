def lesson3(args):
    pass


def cash():
    pay = {}
    try:
        with open(lesson3.txt, 'w', encoding="utf-8") as f:
            for line in f:
                pay[line.split()[0]] = float(line.split()[1])
        print("До 20 т получает")
        for name, pay in pay.items():
            if pay < 20000:
                print(name)
            print(f"Средняя зарплата {sum(pay.values()) / len(pay)}")
    except:
        print("Ошибка")
