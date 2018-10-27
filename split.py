'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки.
'''


result=0
index=0

list = [int(i) for i in input().split()]

for i in list:
  result += i

print(result)