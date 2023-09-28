import math 


def plus (a, b):
    return a + b


def minus(a, b):
    return a - b


def umnojit(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Делить на ноль нельзя."
    else:
        return a / b


def ctepen(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Квадратный корень из отрицательного числа нельзя найти."
    else:
        return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Факториал отрицательного числа не определен."
    elif a == 0:
        return 1
    else:
        return math.factorial(a)


def sine(a):
    return math.sin(a)


def cosine(a):
    return math.cos(a)


def tangent(a):
    return math.tan(a)

def check_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print(" введите число")

def check_symbol_input(prompt):
    while True:
        symbol = input(prompt)
        if len(symbol) == 1:
            return symbol
        else:
            print(" введите только один символ.")


def check_operation_input(prompt):
    operations = ["+", "-", "*", "/", "^", "sqrt", "!", "sin", "cos", "tan"]
    while True:
        operation = input(prompt)
        if operation in operations:
            return operation
        else:
            print(" указанной вами операции нет")


def calculator():
    print("Инженерный калькулятор")
    a = check_number_input("Введите  число , с которым хотите совершать действия ")
    operation = check_operation_input("Введите операцию (+, -, *, /, ^, sqrt, !, sin, cos, tan): ")

    if operation in ["sqrt", "!", "sin", "cos", "tan"]:
        if operation == "sqrt":
            result = square_root(a)
        elif operation == "!":
            result = factorial(a)
        elif operation == "sin":
            result = sine(a)
        elif operation == "cos":
            result = cosine(a)
        elif operation == "tan":
            result = tangent(a)
            
        print(f"Результат: {result}")
    else:
        b = check_number_input("Введите второе число: ")

        if operation == "+":
            result = plus(a, b)
        elif operation == "-":
            result = minus(a, b)
        elif operation == "*":
            result = umnojit(a, b)
        elif operation == "/":
            result = division(a, b)
        elif operation == "^":
            result = ctepen(a, b)

        print(f"Результат: {result}")


calculator()



