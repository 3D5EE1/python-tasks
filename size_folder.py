import os
import sys

commands = sys.argv[1:]

folder_list = [i for i in os.walk('.')]
key_list = ['.', './', '--no-files', '--no-folder', '-h', '--help', '-K', '--Kb', '-M', '--Mb', '-G', '--Gb',]


class SizeFolder:
    sum = 0

    def __init__(self, units, folders=None):

        self.units = units
        if self.units == 'Kb':
            self.factor = 1000
        elif self.units == 'Mb':
            self.factor = 1000000
        elif self.units == 'Gb':
            self.factor = 1000000000

        if folders is None:
            self.folders = folder_list[0][1]
        else:
            self.folders = folders

    @staticmethod
    def get_size(params):
        total_size = 0
        for dir_path, dir_names, file_names in os.walk(params):
            for f in file_names:
                fp = os.path.join(dir_path, f)
                total_size += os.path.getsize(fp)
        return total_size

    def size_b(self):
        print(f'{self.units}\t\tElements\n')
        for i in self.folders:
            size = self.get_size(i)
            print(f'{round(size/self.factor, 2)}\t\t{i}')
            self.sum += size
        print(f'\n{round(self.sum/self.factor, 2)}\tsize all folders\n')

    def size_files(self):
        if folder_list[0][2] is not None:
            for i in folder_list[0][2]:
                size = os.path.getsize(i)
                print(f'{round(size/self.factor, 2)}\t\t{i}')
                self.sum += size
            print(f'\n{round(self.sum/self.factor, 2)}\t\tsize all files')

    @staticmethod
    def help():
        print('Использование: python size_folder.py [КЛЮЧ]… [ФАЙЛ]…\n\n'
              'Суммирует использование дискового пространства набора ФАЙЛОВ,\n'
              'рекурсивно с каталогами.\n\n'
              'Аргументы, обязательные для длинных ключей, обязательны и для коротких.\n\n'
              '   -h, --help       вызов помощи                                    \n'
              '   -K, --Kb         размер элементов текущей директории в килобайтах\n'
              '   -K, --Mb         размер элементов текущей директории в мегобайтах\n'
              '   -G, --Gb         размер элементов текущей директории в гигабайтах\n'
              '   --no-files       размер только папок\n'
              '   --no-folders     размер только файлов\n')


def main():
    if len(commands) == 0:
        SizeFolder('Kb').size_b()
        SizeFolder('Kb').size_files()
    elif len(commands) == 1:
        if commands[0] in key_list[:3]:
            SizeFolder('Kb').size_b()
            SizeFolder('Kb').size_files()
        elif commands[0] in key_list[4:6]:
            SizeFolder('Kb').help()

    else:
        print(f'что-то пошло не так, воспользуйтесь помощью: -h или --help')


if __name__ == '__main__':
    main()




