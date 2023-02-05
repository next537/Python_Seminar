# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
#
# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

n = int(input("Введите n - "))
x = int(input("x - "))
y = int(input("y - "))

list_num = []

for i in range(-n, n+1):
    list_num.append(i)
mult = list_num[x] * list_num[y]
print(list_num)
print(x, y)
print(mult)