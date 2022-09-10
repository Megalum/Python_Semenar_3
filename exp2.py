# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_input = []
dimension_input = int(input('Введите размерность списка: '))
list_output = []
dimension_output = dimension_input / 2
if(dimension_input % 2 == 1):
    dimension_output += 1

for i in range(dimension_input):
    list_input.append(int(input(f'{i} позиция = ')))
for i in range(int(dimension_output)):
    list_output.append(int(list_input[i] * list_input[dimension_input - i - 1]))
print(f'{list_input} => {list_output}')