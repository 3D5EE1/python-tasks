'''
Выведите таблицу размером n x n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной
по часовой стрелке, как показано в примере (здесь n = 5 ):
'''

a = int(input())
b = ([[0 for j in range(a)] for i in range(a)])
n = 1
x1 = 0
y1 = 0
for ii in range(a//2+1):
  for di in range(x1,a-y1):
    b[ii][di] = n
    n +=1
  for di in range(x1+1,a-y1):
    b[di][a-(1+ii)] = n
    n +=1
  for di in range(-(2+x1),-(a+1-y1),-1):
    b[a-(1+ii)][di] = n
    n +=1
  for di in range(-(2+x1),-(a-y1),-1):
    b[di][ii] = n
    n +=1
    x1 += 1
    y1 += 1

for i in range(a):
  for j in range(a):
    print(b[i][j], end=' ')
    print()