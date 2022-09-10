# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

dimension = int(input('Введите размерность списка: '))
fibonacci_left = [1]
fibonacci_right = [1,1]

for i in range(2, dimension):
    fibonacci_right.append(int(fibonacci_right[i - 2] + fibonacci_right[i - 1]))
for i in range(1, dimension):
    fibonacci_left.append(int(fibonacci_right[i]))
    if(fibonacci_left[i - 1] > 0):
        fibonacci_left[i] *= -1
for i in range(dimension // 2):
    fibonacci_left[i], fibonacci_left[dimension - 1 - i] = fibonacci_left[dimension - 1 - i], fibonacci_left[i]

# Для вывода:
fibonacci_left.append(0)
for i in fibonacci_right:
    fibonacci_left.append(i)
print(fibonacci_left)