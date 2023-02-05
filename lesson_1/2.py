# Напишите программу, которая на вход принимает
# 5 чисел и находит максимальное из них


maxNum = 0
for i in range(5):
    num = int(input())
    if num > maxNum:
            maxNum = num
print(maxNum)