import math

x1 = float(input("Введите 1 точку: "))
y1 = float(input("Введите 2 точку: "))
x2 = float(input("Введите 3 точку: "))
y2 = float(input("Введите 4 точку: "))

one = (x1 - x2)**2
two = (y1 - y2)**2

distance = math.sqrt(one + two)

print(distance)
