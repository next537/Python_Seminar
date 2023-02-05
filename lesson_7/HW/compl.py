def make_complex():
    while True:
        a = (input("Введите действительную часть числа: "))
        if not (a.isdigit()):
            print('Повторите ввод')
            continue
        a = int(a)
        break
    while True:
        b = (input("Введите мнимую часть числа: "))
        if not (b.isdigit()):
            print('Повторите ввод')
            continue
        b = int(b)
        break
    return complex(a, b)