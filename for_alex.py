import os

folder_list = [i for i in os.walk('.')]


def get_size(params):
    total_size = 0
    for dir_path, dir_names, file_names in os.walk(params):
        for f in file_names:
            fp = os.path.join(dir_path, f)
            total_size += os.path.getsize(fp)
    return total_size


for i in folder_list[0][1]:
    print(f'{i}\t\t{round(get_size(i)/1000000, 2)} Mb')

for i in folder_list[0][2]:
    print(f'{i}\t\t{round(os.path.getsize(i)/1000, 2)} Kb')