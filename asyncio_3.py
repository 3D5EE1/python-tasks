import asyncio
from concurrent.futures import ProcessPoolExecutor

print('running test')


def func1():
    i = 0
    while True:
        print(f'func1: {i}')
        i += 1


def func2():
    i = 0
    while True:
        print(f'func2: {i}')
        i += 1


def func3():
    i = 0
    while True:
        print(f'func3: {i}')
        i += 1


if __name__ == "__main__":
    executor = ProcessPoolExecutor(3)
    loop = asyncio.get_event_loop()
    test1 = asyncio.ensure_future(loop.run_in_executor(executor, func1))
    test2 = asyncio.ensure_future(loop.run_in_executor(executor, func2))
    test3 = asyncio.ensure_future(loop.run_in_executor(executor, func3))

    loop.run_forever()