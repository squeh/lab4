k = int(input("Введите число мандаринов: "))
n = int(input("Введите число школьников: "))

n_per_student = k // n
n_remainder = k % n

print(f"Количество мандаринов каждому: {n_per_student}")
print(f"Количество мандаринов в остатке: {n_remainder}")
