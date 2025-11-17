import math

x_degrees = float(input())

x_radians = math.radians(x_degrees)

sin_x = math.sin(x_radians)
cos_x = math.cos(x_radians)

tan_x = math.tan(x_radians)
tg_sq_x = tan_x**2

result = sin_x + cos_x + tg_sq_x

print(result)
