﻿""" Program 2Array
    Write by Andrey Pizun """
# Вывод поясняющего текста и предупреждения
print (" -----------------------------------------------------")
print ("| Программа вавода элементов первого списка, квадрат  |")
print ("| которых больше модуля среднеарифметического значения|")
print ("|            элементов второго списка                 |")
print ("|      (Андрей Пизюн 10-H класс, ГБОУ Школа №1474)    |")
print (" -----------------------------------------------------")
print ("")
print ("ВНИМАНИЕ!")
print ("В программе не реализована проверка корректности введения исходных данных.")
print ("Будьте внимательны при вводе!")
print ("")  

# Ввод исходных данных
a = [int(i) for i in input ('Введите через пробел значения первого списка ') .split()]
b = [int(j) for j in input ('Введите через пробел значения второго списка ') .split()]
# Вычисляем модуль среднего арифметического значения элементов второго списка
s = abs(sum(b) / len(b))
# Выводим элемент, удовлетворяющий условию  
for i in range(len(a)):
    if a[i]**2 > s:
        print (a[i])
        
