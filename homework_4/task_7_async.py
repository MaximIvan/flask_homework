from random import randint
import asyncio
import time

start = time.time()

arr = [randint(1, 100) for _ in range(10**6)]

summa = 0

async def sum_num_arr(arr):   
    global summa
    for i in arr:
        summa += i


tasks = []

if __name__ == '__main__':

    
    for i in range(10):
        start_index = i*100_000
        end_index = start_index + 100_000
        task = asyncio.ensure_future( sum_num_arr(arr[start_index:end_index]))
        tasks.append(task)

    loop = asyncio.get_event_loop()  
    loop.run_until_complete(asyncio.wait(tasks)) 

    print('конец завершения  потоков')
    print ('Результат', summa)

    end = time.time()
    print("время выполнения суммы :", end - start)