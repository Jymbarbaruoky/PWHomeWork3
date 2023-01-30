from multiprocessing import cpu_count, Process, RLock as PRlock
from multiprocessing.dummy import Pool
from threading import Thread, RLock as TRlock
from time import time




def factorize(numbers, lock):
    with lock:
        result = []
        for number in numbers:
            res = []
            for n in range(number):
                if n != 0 and number % n == 0:
                    res.append(n)
            result.append(res)
        return result


if __name__ == '__main__':
    print(f'Count CPU: {cpu_count()}')
    values = (128, 255, 99999, 10651060)
    th_lock = TRlock()
    threads = [
        Thread(target=factorize, args=(values, th_lock)),
        Thread(target=factorize, args=(values, th_lock))
    ]
    timer = time()
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f'End two threads: {round(time() - timer, 3)}')

    p_lock = PRlock()
    procecess = [
        Process(target=factorize, args=(values, p_lock)),
        Process(target=factorize, args=(values, p_lock))
    ]
    timer = time()
    [process.start() for process in procecess]
    [process.join() for process in procecess]
    [process.close() for process in procecess]
    print(f'End two procecess: {round(time() - timer, 3)}')

    timer = time()
    with Pool(2) as pool:
        result = pool.starmap(factorize, [(values, th_lock), (values, th_lock)])
    print(f'End two pool procecess: {round(time() - timer, 3)}')


