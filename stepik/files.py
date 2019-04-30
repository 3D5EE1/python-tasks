'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

from stepik import requests

enter = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'

url = 'https://stepic.org/media/attachments/course67/3.6.3/'

r = requests.get(enter)

while True:
  if "We" not in r.text:
    url += r.text
    r = requests.get(url)
    url = 'https://stepic.org/media/attachments/course67/3.6.3/'
  else:
    print(r.text)
    break
