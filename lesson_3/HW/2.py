# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.



from random import randint


size = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(size):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and size > len(list)/2:
        size = size - 1
        a = list[i] * list[size]
        list2.append(a)
        i += 1

print(list)
print(list2)