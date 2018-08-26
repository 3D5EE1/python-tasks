import sys

digit_string = sys.argv[1]

print(sum([int(digit_string[i]) for i in range(len(digit_string))]))

