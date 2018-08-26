def decor(func):
    def wrap(a, b, c):
        print('результат функции:', func(a,b))
        print('число вычитания', c)
        print('результат вычитания:', func(a, b) - c)
    return wrap

a = int(input('введите 1 число: '))
b = int(input('введите 2 число: '))
c = int(input('введите 3 число: '))

print('\nсложим первые два числа и вычтем третье')

@decor
def fisha(a, b):
    return a + b

fisha(a, b, c)

print('\nвычтем первые два числа и вычтем третье')

@decor
def minus(a,b):
    return a - b

minus(a, b, c)

print('\nумножим первые два числа и вычтем третье')

@decor
def umnog(a,b):
    return a * b

umnog(a, b, c)