'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка
вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на
противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список
"13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''


list = [int(i) for i in input().split()]

list.append(list[0])
list.append(list[-2])

result = 0
index = 0

for i in list:
  if len(list) == 3:
    print(list[0])
    break
  if index <= len(list) - 3:
    result = list[index - 1] + list[index + 1]
    index += 1
 print(result, end = ' ')
