# Показать первую цифру дробной части числа
a = float(input("Введите дробное число = "))
c = round(a)
b = round(a, 1)
tmp_result = float(round(((b-c)*10),1))
result = int(tmp_result)
print(result)
