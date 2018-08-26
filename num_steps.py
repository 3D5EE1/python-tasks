import sys

num_steps = int(sys.argv[1])


print(*((' ' * i + '#'* (num_steps - i)) for i in range(num_steps-1, -1, -1)), sep='\n')
