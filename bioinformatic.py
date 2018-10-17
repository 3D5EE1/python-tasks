'''
В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу,
по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), выводящее это число в консоль вместе
с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми,
например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000
человек.

Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. Если ваше решение не проходит какой-то тест, это значит,
что вы не рассмотрели какой-то из случаев входных данных (число программистов 0≤n≤10000≤n≤1000). Обязательно проверяйте свои
решения на дополнительных значениях, а не только на тех, что приведены в условии задания.

Так как задание повышенной сложности, вручную код решений проверяться не будет. Если вы столкнулись с ошибкой в первых четырёх
тестах, проверьте, что вы используете только русские символы для ответа. В остальных случаях ищите ошибку в логике работы
программы.
'''

n = int(input()) #число программистов
p = 'программист'
if 0 <= n <= 1000:
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        print(str(n), p + "а")
    elif n % 10 == 1 and n % 100 != 11:
        print(str(n), p)
    else:
        print(str(n), p + "ов")