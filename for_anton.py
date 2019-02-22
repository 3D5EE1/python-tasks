import sys
import crypt
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


commands = sys.argv[1:]
command = [i for i in commands]

with open(f'{command[0]}', 'r') as login:
    file = login.read()


with open(f'{command[1]}', 'w') as password:
    file = file.split('\n')
    for i in file:
        id = id_generator()
        line = f"  - (login: '{i}',\tpass: '{crypt.crypt(i, id)}', comment: '{command[2]}')\n"
        password.write(line)
