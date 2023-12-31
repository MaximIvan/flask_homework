import os
import random
import time
import multiprocessing

def arr_generator(n: int = 1_000_000):
    arr = []
    for _ in range(n):
        arr.append(random.randint(1, 100))
    return arr


def split_the_array(arr: list, n: int):
    arr_parts = []
    coef = len(arr) // n
    start = 0
    end = 0
    for _ in range(coef):
        if end <= (len(arr) - 1):
            end += coef
            arr_parts.append((start, end - 1))
            start = end
    return arr_parts


def sum_the_array(arr: list, start: int, end: int):
    sum = 0

    for i in range(start, end):
        sum += arr[i]
    with open("sum.txt", "a") as f:
        f.write(str(sum) + '\n')


process_list = []
if __name__ == '__main__':
    rez = []
    start_time = time.time()
    arr = arr_generator(1_000_000)
    arr1 = split_the_array(arr, 100)
    for i in arr1:
        process = multiprocessing.Process(target=sum_the_array, args=(arr, i[0], i[1],))
        process_list.append(process)
        process.start()
    for process in process_list:
        process.join()
    print(f'Время выполнения {time.time() - start_time}')
    with open("sum.txt", "r") as f:
        for line in f:
            rez.append(int(line))
    os.remove("sum.txt")
    print(sum(rez))