'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые
повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''

list = [int(i) for i in input().split()]
list.sort()
list2 = []
count = 0

for i in list:
  if len(list) == 1:
    break
  if list.count(i) > 1:
    i = [i]
    list2 += i

list2.append('end')

for t in list2:
  if count < len(list2) - 1:
    if list2[count] != list2[count + 1]:
        print(t, end= ' ')
        count += 1
