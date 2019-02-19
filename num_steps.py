import my_sys

num_steps = int(my_sys.argv[1])


print(*((' ' * i + '#'* (num_steps - i)) for i in range(num_steps-1, -1, -1)), sep='\n')
