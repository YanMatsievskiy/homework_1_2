'''Задача 2. Простые арифметические вычисления'''

first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')

result = round(((float(first_number) + float(second_number))*3), 2)

print('Итоговый результат:', result)