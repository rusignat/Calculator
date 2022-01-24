def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def division(a, b):
    return a / b
def multiplication(a, b):
    return a * b
def square(a):
    q = int(input("Введите степень, в которую возвести число: "))
    c = a ** q
    return c
def root(a):
    import math
    num = math.sqrt(a)
    return num

print("1 - Сложение\n2 - Вычитание\n3 - Деление\n4 - Умножение\n5 - Ввозвести в степень\n6 - Корень")
a = int(input("Выберите действие: "))
while a > 0 and a < 7:
    if a > 0 and a < 5:
        number_1 = int(input("Первое число: "))
        number_2 = int(input("Второе число: "))
    if a > 4 and a < 7:
        number_3 = int(input("Введите число: "))
    if a == 1:
        print("Ответ:", addition(number_1, number_2))
    elif a == 2:
        print("Ответ:", subtraction(number_1, number_2))
    elif a == 3:
        print("Ответ:", division(number_1, number_2))
    elif a == 4:
        print("Ответ:", multiplication(number_1, number_2))
    elif a == 5:
        print("Ответ:", square(number_3))
    elif a == 6:
        print("Ответ:", root(number_3))
    if a > 0 and a < 7:
        a = int(input("выберите действие: "))
while a < 1 or a > 6:
    a = int(input("Выберите действие: "))
    while a > 0 and a < 7:
        if a > 0 and a < 5:
            number_1 = int(input("Первое число: "))
            number_2 = int(input("Второе число: "))
        if a > 4 and a < 7:
            number_3 = int(input("Введите число: "))
        if a == 1:
            print("Ответ:", addition(number_1, number_2))
        elif a == 2:
            print("Ответ:", subtraction(number_1, number_2))
        elif a == 3:
            print("Ответ:", division(number_1, number_2))
        elif a == 4:
            print("Ответ:", multiplication(number_1, number_2))
        elif a == 5:
            print("Ответ:", square(number_3))
        elif a == 6:
            print("Ответ:", root(number_3))
        if a > 0 and a < 7:
            a = int(input("Ввыберите действие: "))