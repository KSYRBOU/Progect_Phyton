# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
a = int(input("Введите число a = "))
first_condition = a % 5
second_condition = a % 10
third_condition = a % 15
fourth_condition = a % 30
if first_condition == 0 and (second_condition == 0 or third_condition == 0) and fourth_condition > 0:
    print(f"Число a = {a} кратно 5 и 10 или 15 но не 30!")
else:
    print(f"Число a = {a} не кратно 5 и 10 или 15 но не 30!")