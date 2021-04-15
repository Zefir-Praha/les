from sys import argv

def wage():
    try:
        hours, rate, bonus = map(float, argv[1:])
        print(f"salary - {hours * rate + bonus}")
    except ValueError:
        print("Данные для расчета")
wage()