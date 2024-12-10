import random

my_list = [random.randint(0, 100) for i in range(random.randint(3, 10))]
print("Сгенерований список:", my_list)

if len(my_list) >= 3:
    my_list_2 = [my_list[0], my_list[2], my_list[-2]]
print("Новий список 3 елементів початкового списку - першим, третім і другим з кінця:", my_list_2)