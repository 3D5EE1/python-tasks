import my_sys

digit_string = my_sys.argv[1]

print(sum([int(digit_string[i]) for i in range(len(digit_string))]))

