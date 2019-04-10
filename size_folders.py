import os
import sys


class Size:
    folder_list = [i for i in os.walk('.')]

    def __init__(self, units, folders=None, files=None):

        self.units = units

        if folders is None:
            self.folders = self.folder_list[0][1]
        else:
            self.folders = folders

        if files is None:
            self.files = self.folder_list[0][2]
        else:
            self.files = files

    @staticmethod
    def get_size(params):
        total_size = 0
        for dir_path, dir_names, file_names in os.walk(params):
            for file in file_names:
                file_path = os.path.join(dir_path, file)
                total_size += os.path.getsize(file_path)
        return total_size

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

    def factor(self):
        if self.units == 'Kb':
            return 1000
        elif self.units == 'Mb':
            return 1000000
        elif self.units == 'Gb':
            return 1000000000


class SizeFolders(Size):

    def size_folders(self):
        sum_folders = 0
        if self.folders is not None:
            for i in self.folders:
                size = self.get_size(i)
                print(f'{round(size/self.factor(), 2)}\t\t{i}')
                sum_folders += size
            return sum_folders/self.factor()


class SizeFiles(Size):

    def size_files(self):
        sum_files = 0
        if self.files is not None:
            for i in self.files:
                size = os.path.getsize(i)
                print(f'{round(size/self.factor(), 2)}\t\t{i}')
                sum_files += size
        return sum_files/self.factor()


class SizeAll(SizeFolders, SizeFiles):

    def size_all(self):
        print(f'{self.units}\t\tElements')
        sum_folder = self.size_folders()
        sum_files = self.size_files()
        print(f'~~~~~~~~~~~~~~~~~~~~~~~\n{round(sum_folder + sum_files, 2)}')


commands = sys.argv[1:]
keys = {'.':'',
        './':'',
        '--no-files':'',
        '--no-folders':'',
        '-h':'',
        '--help':'',
        '-K':'',
        '--Kb':'',
        '-M':'',
        '--Mb':'',
        '-G':'',
        '--Gb':'', }


def main():
    if len(commands) == 0:
        SizeAll('Kb').size_all()


if __name__ == '__main__':
    main()

