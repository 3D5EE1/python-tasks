'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и выведет
"Счастливый", если суммы совпадают, и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
'''

number = str(input()) #число
first = int(number) // 1000
last = int(number) % 1000
if first // 100 + first // 10 % 10 + first % 10 == last // 100 + last // 10 % 10 + last % 10:
  print('Счастливый')
else:
  print('Обычный')