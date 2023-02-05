# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности в том же порядке.


from random import randint


def list_rand_nums(count: int):
    if count <= 0:
        print("Negative value of the number of numbers!")
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randint(1, 10))

    return list_nums


list = list_rand_nums(int(input("Введите количество чисел: ")))
print(list)

print("Вывод: ")
for k in list:
    if list.count(k) == 1:
        print(k, end=" ")