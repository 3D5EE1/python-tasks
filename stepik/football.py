'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на
стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число  n— количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:

Зенит:2 2 0 0 6
Спартак:2 0 1 1 1
ЦСКА:2 0 1 1 1
'''

a = int(input())
l = []
for i in range(a):
  l.append(str(input()).split(';'))

def games(x):
  games = 0
  for i in range(len(l)):
    if x in l[i]:
        games += 1
  return games

def wins(x):
  wins = 0
  for i in range(len(l)):
    if x in l[i]:
        if x == l[i][0] and l[i][1] > l[i][3]:
            wins += 1
    elif x == l[i][2] and l[i][1] < l[i][3]:
        wins += 1
  return wins

def defeats(x):
  defeats = 0
  for i in range(len(l)):
    if x in l[i]:
        if x == l[i][0] and l[i][1] < l[i][3]:
            defeats += 1
    elif x == l[i][2] and l[i][1] > l[i][3]:
        defeats += 1
  return defeats

def draws(x):
  draws = 0
  for i in range(len(l)):
    if x in l[i] and l[i][1] == l[i][3]:
        draws += 1
  return draws

def count():
  count = int(wins(team)) * 3 + int(draws(team)) * 1
  return count

d= {}

for i in range(a):
  team = str(l[i][0])
  d[team] = [games(team), wins(team), draws(team), defeats(team), count()]
  team = str(l[i][2])
  d[team] = [games(team), wins(team), draws(team), defeats(team), count()]

for key, v in d.items():
  print(f'{key}:{v[0]} {v[1]} {v[2]} {v[3]} {v[4]}')
