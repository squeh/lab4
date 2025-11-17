import math

seat_number = int(input("Введите свое место (1-36): "))
if 1 <= seat_number <= 36:
    compartment_number = math.ceil(seat_number / 4)
    print(int(compartment_number))
else:
    print("Вы ввели неверное число.")
