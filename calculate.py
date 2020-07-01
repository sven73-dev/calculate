num1 = float(input('Первое число: '))
num2 = float(input('Второе число: '))
Operation = input('Операция: ')

if Operation == '+':
    print(num1 + num2)
if Operation == '-':
    print(num1 - num2)
if Operation == '/' and num2 == 0.0:
    print('Деление на 0!')
if Operation == '/' and num2 != 0:
    print(num1 / num2)
if Operation == '*':
    print(num1 * num2)
if Operation == 'pow':
    print(num1 ** num2)
if Operation == 'div' and num2 == 0.0:
    print('Деление на 0!')
if Operation == 'div' and num2 != 0.0:
    print(num1 // num2)
if Operation == 'mod' and num2 == 0.0:
    print('Деление на 0!')
if Operation == 'mod' and num2 != 0.0:
    print(num1 % num2)