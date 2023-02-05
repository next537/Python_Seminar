def take_number():
    value = input('Введите число: ')
    try:
        value = float(value)
        return value
    except ValueError:
        print('Это не число')
        return take_number()