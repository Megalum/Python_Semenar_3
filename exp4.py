# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
binary = []
count = 0

while number != 0:
    binary.append(int(number % 2))
    number = int((number - binary[count]) // 2)
    count += 1
for i in range(count // 2):
    binary[i], binary[count - 1 - i] = binary[count - 1 - i], binary[i]
print(binary)