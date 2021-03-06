"""Общее описание:
Бригада застройщика вывозит строительный мусор:)
Мусор рапределен по мешкам (кол-во мешков от 1 до 40).
У каждого мешка известен вес в килограммах (от 1 до 100 кг).
Необходимо все мешки распределить по 2-м кучам, таким образом,
чтобы разница весов полученных куч было минимальным.

Техническое описание:
Необходимо написать функцию, на вход которой приходит список весов всех мешков.
На выходе функция должна возвращать положительное число, разницу весов полученных куч.

Примеры:
f([1,2,3]) = 0
f([1,1,1,4]) = 1
"""


def f(garbage):
    try:
        if min(garbage) < 1 or max(garbage) > 100 or not 1 <= len(garbage) <= 40:
            raise ValueError
        else:
            garbage.sort()
            garbage.reverse()
            mean = sum(garbage) / 2
            max_value = []
            for i in garbage:
                new_list = garbage.copy()
                new_list.remove(i)
                for j in new_list:
                    if i + j < mean:
                        i += j
                max_value.append(i)
            return abs(sum(garbage) - max(max_value) * 2)
    except ValueError:
        return 'Ваши данные не удовлетворяют условию задачи: "кол-во мешков от 1 до 40", "вес мешков от 1 до 100 кг"'


if __name__ == '__main__':
    assert f([]) == 'Ваши данные не удовлетворяют условию задачи: ' \
                    '"кол-во мешков от 1 до 40", "вес мешков от 1 до 100 кг"', "First"
    assert f([i for i in range(1, 42)]) == 'Ваши данные не удовлетворяют условию задачи: ' \
                                           '"кол-во мешков от 1 до 40", "вес мешков от 1 до 100 кг"', "Second"
    assert f([0]) == 'Ваши данные не удовлетворяют условию задачи: ' \
                     '"кол-во мешков от 1 до 40", "вес мешков от 1 до 100 кг"', "Third"
    assert f([101]) == 'Ваши данные не удовлетворяют условию задачи: ' \
                       '"кол-во мешков от 1 до 40", "вес мешков от 1 до 100 кг"', "Fourth"
    assert f([1, 1, 1, 4]) == 1, "Fifth"
    assert f([1, 2, 3]) == 0, 'Sixth'
    assert f([5, 12, 6, 44, 23]) == 2, 'Seventh'
    assert f([100, 100, 50]) == 50, 'Eighth'
    assert f([50, 51]) == 1, 'Ninth'
    assert f([80, 1, 1]) == 78, 'Tenth'
    assert f([30, 100, 20]) == 50, 'Eleventh'
    assert f([17, 44, 12, 6, 1, 35, 8]) == 1, 'Twelfth'


