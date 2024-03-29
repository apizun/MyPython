﻿""" Python3 program > 2Array
    Written by Andrey Pizun """

# Вывод поясняющего текста и предупреждения
print ("\n\t -----------------------------------------------------")
print ("\t|      Программа вывода элементов первого списка,     |")
print ("\t| квадрат которых больше модуля среднеарифметического |")
print ("\t|         значения элементов второго списка           |")
print ("\t|      (Андрей Пизюн 10-H класс, ГБОУ Школа №1474)    |")
print ("\t -----------------------------------------------------\n")

print ("ВНИМАНИЕ!")
print ("В программе не реализована проверка корректности введения исходных данных.")
print ("Будьте внимательны при вводе!\n")

# Ввод исходных данных
qa = int (input ("Введите количество элементов в первом списке - "))
qb = int (input ("Введите количество элементов во втором списке - "))
min = int (input ("Введите минимальное значение элемента в списке - "))
max = int (input ("Введите максимальное значение элемента в списке - "))
print ()
import random # подключаем модуль генератора случайных чисел
a = random.sample(range(min,max), qa)
b = random.sample(range(min,max), qb)
print ("Первый список - ", a)
print ("Второй список - ", b,"\n")
# Вычисляем модуль среднего арифметического значения элементов второго списка
s = abs(sum(b) / len(b))
# Выводим элемент, удовлетворяющий условию  
for i in range(len(a)):
    if a[i]**2 > s:
        print ('[',i,'] - ',a[i])
print ("\nРабота программы завершена\n")        

