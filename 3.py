number = int(input("Введите 4х значное число(пример: 1500): "))

thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10

# Вывод результата в соответствии с примером
print(f"Цифра в позиции тысяч равна {thousands}")
print(f"Цифра в позиции сотен равна {hundreds}")
print(f"Цифра в позиции десятков равна {tens}")
print(f"Цифра в позиции единиц равна {units}")
