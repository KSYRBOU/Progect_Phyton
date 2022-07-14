#Найти максимальное из пяти чисел
a = int(input("Введите число a = "))
b = int(input("Введите число b = "))
c = int(input("Введите число c = "))
d = int(input("Введите число d = "))
e = int(input("Введите число e = "))
max = a
#if b > max:
#    max = b
#if c > max:
#    max = c
#if d > max:
#    max = d
#if e > max:
#    max = e
#print(f"Максимальное число = {max}!")

for i in [b, c, d, e]:
    if max < i:
        max = i
print(f"Максимальное число = {max}!")
