list_cars = ['bugatti', 'mercedes-benz', 'lada', 'peugeot', 'maybach', 'lamborghini', 'koenigsegg']


list_cars_sorted = sorted(list_cars, key=len)

for i in list_cars_sorted[::-1]:
    print('{0:.>20}'.format(i))

print()

print(*['.'*10+(len(list_cars_sorted[-1])-len(i))*'.'+i for i in list_cars_sorted[::-1]], sep='\n')

