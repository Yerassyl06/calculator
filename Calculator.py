from math import *
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))


op = input('Выберите операцию (Введите +, -, *, /):\n '

                '+ - сложение двух чисел\n'

                '- - вычитание двух чисел\n'

                '* - умножение двух чисел\n'

                '/ - деление двух чисел\n')

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("Неверная операция")
