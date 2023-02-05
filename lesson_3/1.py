# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя.

import os
clear = lambda: os.system('cls')
clear()

# 1 способ - import random
from random import sample #2 способ

def find_number (amount, user_number):
    new_list = sample(range(1, (amount+1)*2), k=amount) # для 1го способа random.sample
    print((new_list))
    if user_number in new_list:
        return "yes"
    return "no"

some_number = find_number(int(input("Enter amount - ")), int(input("Enter the desired number - ")))

print(some_number)