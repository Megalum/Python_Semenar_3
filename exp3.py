# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_input = []
list_output = []
dimension = int(input('Введите размерность списка: '))

for i in range(dimension):
    list_input.append(float(input(f'{i} позиция = '))) 

for i in list_input:
    if (i // 1 != i):
        list_output.append(round(float(i - (i // 1)).real, 10)) 

max, min = list_output[0], list_output[0]
for i in list_output:
    if(min > i):
        min = i
    if(max < i):
        max = i
print(f'{list_input} => {max - min}')