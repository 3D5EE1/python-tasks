import os


def draw_canvas(clear=None) -> None:

    my_list[y][x] = 'O'

    if clear is None:
        pass
    else:
        os.system('cls')

    for i in my_list:
        print(*i, end='\n')

    my_list[y][x] = '+'


exit_cursor = True

res: list = input('введите два числа через пробел, которые зададут размер холста: ').split()

my_list = [['+' for i in range(int(res[0]))] for j in range(int(res[1]))]

x = len(my_list[0]) // 2
y = len(my_list) // 2

print(f'вы находитесь в положении ( x:{x}, y:{y} )\n')

my_list[y][x] = 'O'

draw_canvas()

while exit_cursor:
    cursor: str = input('\nввудите \'w\',\'s\',\'a\',\'d\' для движения внутри квадрата или \'exit\' для выхода : ')
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

    draw_canvas('clear')






