'''
Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.

Пример работы программы:
'''

'''
> python3 my_solution.py arg1 arg2
arg1 arg2
'''

import sys

c = sys.argv[1:]

for i in range(len(c)):
    print(c[i], end=" ")
