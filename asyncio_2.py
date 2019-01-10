import asyncio
import time


async def func1():
    print(f'первая сопрограмма: сообщение первое {time.asctime()}')
    await asyncio.sleep(.6)
    print(f'первая сопрограмма: сообщение второе {time.asctime()}')


async def func2():
    print(f'вторая сопрограмма: сообщение первое {time.asctime()}')
    await asyncio.sleep(.8)
    print(f'вторая сопрограмма: сообщение второе {time.asctime()}')


async def func3():
    print(f'третья сопрограмма: сообщение первое {time.asctime()}')
    await asyncio.sleep(1.2)
    print(f'третья сопрограмма: сообщение второе {time.asctime()}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(func1(), func2(), func3()))