# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci_list(k: int):
    x, y = 1, 1
    fib_list = [0]
    for i in range(k):
        fib_list.append(x)
        fib_list.insert(0, x * (-1) ** i)
        x, y = y, y + x
    return fib_list

k = 0
while k < 2:
    k = int(input('Введите число больше чем 2: '))
    if k < 2:
        print('Введите число больше чем 2!')
fib_list = fibonacci_list(k)
print(fib_list)