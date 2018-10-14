'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию,
после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
'''

a = float(input()) #первое чисто
b = float(input()) #второе число
c = input() #действие
if c == '+':
  result = a + b
  print(result)
elif c == '-':
  result = a - b
  print(result)
elif c == '*':
  result = a * b
  print(result)
elif c == '/' and b != 0:
  result = a / b
  print(result)
elif c == 'mod' and b != 0:
  result = a % b
  print(result)
elif c == 'pow':
  result = a ** b
  print(result)
elif c == 'div' and b != 0:
  result = a // b
  print(result)
elif b == 0:
  print("Деление на 0!")
