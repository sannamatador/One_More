import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач', name, 'начал соревнования.')
    for i in range(1, 6):
       print(f'Силач', name, 'поднял', i)
       await asyncio.sleep(1/power)
    print(f'Силач', name, 'закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('John', 3))
    task2 = asyncio.create_task(start_strongman('Paul', 4))
    task3 = asyncio.create_task(start_strongman('Ringo', 6))
    await task1
    await task2
    await task3


if __name__ == '__main__':
    asyncio.run(start_tournament())
