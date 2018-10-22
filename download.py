import time
from tqdm import tqdm


n = input('Хотите сделать все хорошо ?\n'
          'если да, то напишите "yes"\n'
          'иначе напишите "no"\n'
          'сделайте выбор: ')
print()

if n == 'yes':
    for i in tqdm(range(100), ncols = 130):
         time.sleep(0.025)
    print('\nХорошо сделано !!!\n')
else:
    print('ну и ладно')