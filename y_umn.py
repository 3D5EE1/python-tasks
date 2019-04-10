from functools import reduce

first_str = '7 60 4'.split()
second_str = '30 1 1 3 10 6 4'.split()

# first_str = '7 27 2'.split()
# second_str = '9 1 1 27 3 27 3'.split()

first_str = [int(i) for i in first_str]
second_str = [int(i) for i in second_str]
list_A = [int(i) for i in second_str]
list_A.sort()

result = []

for i in list_A[::-1]:
    result = [i]
    for j in list_A[::-1]:
        if reduce(lambda x, y: x*y, result) * j <= first_str[1] and len(result) <= first_str[2]-1:
            result.append(j)
    if reduce(lambda x, y: x*y, result) == first_str[1]:
        break
count = 0

for i in range(first_str[0]):
    if second_str[i] in result and count < first_str[2]:
        result.pop(result.index(second_str[i]))
        print(i+1, end=' ')
        count += 1



'''
first_str = input().split()
second_str = input().split()

first_str = [int(i) for i in first_str]
list_A = [int(i) for i in second_str]

multiples_M = [i for i in range(1, 10) if first_str[1] % i == 0 and i in list_A]
multiples_M.append(first_str[1])

for i in multiples_M:
    for j in multiples_M[:-1]:
        if i * j == first_str[1]:
            print(list_A.index(i)+1, list_A.index(j)+1)
        break
        
// print(*[second_str.index(i)+1 for i in result])

----------------------------------------

first_str = input().split()
second_str = input().split()

first_str = [int(i) for i in first_str]
second_str = [int(i) for i in second_str]
list_A = [int(i) for i in second_str]
list_A.sort()

result = []

for i in list_A[::-1]:
    result = [i]
    for j in list_A[::-1]:
        if reduce(lambda x, y: x*y, result) * j <= first_str[1] and len(result) <= first_str[2]-1:
            result.append(j)
    if reduce(lambda x, y: x*y, result) == first_str[1]:
        break
for i in range(first_str[0]):
    if second_str[i] in result:
        print(i+1, end=' ')
'''

