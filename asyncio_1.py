import random
import asyncio


async def produce():
    await asyncio.sleep(.5)
    data = random.randint(1, 100)
    return data

async def consume():
    sum_ = 0
    count = 0

    while True:
        data = await produce()
        print('Got data:', data)

        sum_ += data
        count += 1

        print('Sum:', sum_)
        print('Average:', sum_ / count)
        print()


async def another_task():
    while True:
        print()
        print('Hello from another task!')
        print()
        await asyncio.sleep()


if __name__ == '__main__' :
    loop = asyncio.get_event_loop()
    tasks = [consume(), another_task()]
    loop.run_until_complete(asyncio.wait(tasks))