import asyncio


async def func1(future):
    print('старт первой сопрограммы')
    await asyncio.sleep(1.6)
    future.set_result(f'результат первой сопрограммы')


async def func2():
    print(f'старт второй сопрограммы')
    await asyncio.sleep(.8)
    print(f'результат второй сопрограммы')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func1(future))
    loop.run_until_complete(asyncio.gather(future, func2()))

    print(future.result())
    loop.close()