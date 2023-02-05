# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math

xa = int(input("Введите точку xa - "))
xb = int(input("Введите точку xb - "))

ya = int(input("Введите точку ya - "))
yb = int(input("Введите точку yb - "))

distance = math.sqrt(math.pow((xb - xa), 2) + math.pow((yb - ya), 2))
print(distance)