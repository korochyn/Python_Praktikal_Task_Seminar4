# Урок 4. Словари, множества и профилирование
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Ведите количество элементов первого списка :'))
list_n = list() 
for i in range(n):
    n1 = int(input('Введите элемент первого списка :'))
    list_n.append(n1)
print(f'Вы ввели вот такой первый список: {list_n}')
set_n = set(list_n)
print(f'Вы получили вот такое первое множество: {set_n}')

m = int(input('Ведите количество элементов второго списка :'))
list_m = list() 
for i in range(m):
    m1 = int(input('Введите элемент второго списка :'))
    list_m.append(m1)
print(f'Вы ввели вот такой второй список: {list_m}')
set_m = set(list_m)
print(f'Вы получили вот такое второе множество: {set_m}')


set_n_m = set_n.intersection(set_m)
print(f'Вы получили вот такое множество: {set_n_m}')
list_n_m = list(set_n_m)
print(f'Вы получили вот токой не сортированный список: {list_n_m}')
list_n_m_sorted = sorted(list_n_m)
print(f'Вы получили вот токой сортированный список: {list_n_m_sorted}')

