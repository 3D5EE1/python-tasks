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
