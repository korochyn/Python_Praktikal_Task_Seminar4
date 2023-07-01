# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# Сочиняем количество ягод на кустах
import random
max = 1000 # максимальное количество ягод на кусту
min = 1 # минимальное количество ягод на кусту
list_tmp = list(range(min,max))
random.shuffle(list_tmp)
n = 33 # поскольку за один проход собирающий модуль собирает ягоды с 3 кустов то будем считать что число кустов делиться на 3 без остатка
list_berries = list_tmp[0:n]

print(f'Имеется {n} штуки кустов на которых растут ягоды в таком порядке :')
print(list_berries)
list_assembling = list()
i=0
while i < n :
    tmp = list_berries[i] + list_berries[i+1] + list_berries[i+2]
    list_assembling.append(tmp)
    i = i + 3
print()
print(f'С грядки за {n//3} заходов сборщиком было собрано ')
print (list_assembling)
print()
max = list_assembling[0]
for i in range(n//3):
    if list_assembling[i] > max:
        max = list_assembling[i]
print (f' Максимальное количество ягод собранных за один заход = {max} ')
