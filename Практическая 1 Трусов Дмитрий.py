
try:
    x = int(input("Введите первое число"))
    y = int(input("Введите второе число"))
    num_list = [1, 2, 3, 4, 5]
    result = x + y
    print(f"Сложение: {x} + {y} = {result} ")
    result = x - y
    print(f"Вычитание: {x} - {y} = {result} ")
    result = x * y
    print(f"Умножение: {x} * {y} = {result} (")
    try:
        result = x / y
        print(f"Деление: {x} / {y} = {result:.2f} ")
    except ZeroDivisionError:
        print("Ошибка при деление на ноль!")
    result = x // y
    print(f"Целочисленное деление: {x} // {y} = {result} ")
    result = x % y
    print(f"Остаток от деления: {x} % {y} = {result} ")
    result = x ** y
    print(f"Возведение в степень: {x} в степень {y} = {result} ")

    print("\n2 Операторы сравнения \n")
    if x == y:
        print(f"Равно: {x} == {y}  Верно")
    else:
        print(f"Равно: {x} == {y}  Неверно")
    if x != y:
        print(f"Не равно: {x} != {y} Верно")
    else:
        print(f"Не равно: {x} != {y} Неверно")

    if x > y:
        print(f"Больше: {x} > {y} Верно")
    else:
        print(f"Больше: {x} > {y} Неверно")
    if y < x:
        print(f"Меньше: {y} < {x} Верно")
    else:
        print(f"Меньше: {y} < {x} Неверно")
    if x >= y:
        print(f"Больше или равно: {x} >= {y} Верно")
    else:
        print(f"Больше или равно: {x} >= {y} Неверно")
    if y <= x:
        print(f"Меньше или равно: {y} <= {x} Верно")
    else:
        print(f"Меньше или равно: {y} <= {x} Неверно")

    print("\n Логические операторы:\n")
    if (x > 10) and (y < 5):
        print(f" ({x} > 10) и ({y} < 5) Верно")
    else:
        print(f" ({x} > 10) и ({y} < 5) Неверно")
    if (x < 10) or (y > 5):
        print(f"или: ({x} < 10) или ({y} > 5)Верно")
    else:
        print(f" ({x} < 10) или ({y} > 5) Неверно")
    if not (x == y):
        print(f" не ({x} == {y}) Верно")
    else:
        print(f" не ({x} == {y}) Неверно")


    print("\nПобитовые операторы\n")
    a = int(input("Введите первое число для второй части калькулятора"))
    b = int(input("Введите второе число для второй части калькулятора"))
    result = a & b
    print(f"Побитовое и: {a} & {b} = {result} ")
    result = a | b
    print(f"Побитовое или: {a} | {b} = {result} ")
    result = a ^ b
    print(f"Побитовое исключающие или(XOR): {a} ^ {b} = {result}")
    result = ~a
    print(f"Побитовое НЕ: ~{a} = {result}")
    result = a << 2
    print(f"Сдвиг влево: {a} << 2 = {result} ")
    result = a >> 1
    print(f"Сдвиг вправо: {a} >> 1 = {result} (равно 5)")
    print("\n Операторы принадлежности\n")
    d=int(input("Введите число для третий части калькулятора"))

    if d in num_list:
        print(f" {d} В {num_list} Верно")
    else:
        print(f" {d} В {num_list} Неверно")
    if d not in num_list:
        print(f" {d} not in {num_list} Верно")
    else:
        print(f" {d} not in {num_list} Неверно")
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1


    if list1 is list3:
        print(f"Список 1 и список 2 одинаковые(верно)")
    else:
        print(f"Список 1 и список 2 разные(неверно)")


    if list1 is not list2:
        print(f"Список 1 и список 2 одинаковые(неверно)")
    else:
        print(f"Список 1 и список 2 одинако 9вые(верно)")

    if x is y:
        print(f"{x} и {y} одно и тоже значение")
    else:
        print(f"{x} и {y} Разные значения")

except Exception as e:
    print(f"\nПроизошла ошибка: {e}")

finally:
    print("Программа сработа успешно без ошибок")
