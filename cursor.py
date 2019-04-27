import os

x = 0
y = 0
exit_cursor = True

res: list = input('введите размер квадрата, два числа через пробел: ').split()
my_list = [['+' for i in range(int(res[0]))] for j in range(int(res[1]))]
print('вы находитесь в положении ( 0 : 0 )\n')
my_list[y][x] = 'O'

for i in my_list:
    print(*i, end='\n')
my_list[y][x] = '+'

while exit_cursor:
    cursor: str = input('\nввудите \'w\',\'s\',\'a\',\'d\' или \'exit\' для выхода для движения внутри квадрата: ')
    print()
    if cursor == 'exit':
        exit_cursor = False
        break

    elif cursor == 'd':
        x += 1
        if x > len(my_list[y])-1:
            x = 0

    elif cursor == 'a':
        x -= 1
        if x < 0:
            x = len(my_list[y])-1

    elif cursor == 'w':
        y -= 1
        if y < 0:
            y = len(my_list)-1

    elif cursor == 's':
        y += 1
        if y > len(my_list)-1:
            y = 0

    elif cursor not in ['w', 's', 'a', 'd']:
        print('вы ввели не верное значение')
        continue

    my_list[y][x] = 'O'
    os.system('cls')
    for i in my_list:
        print(*i, end='\n')
    my_list[y][x] = '+'




