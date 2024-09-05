import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor


def inc(counter, value=1):
    counter.value += value


def calculate(lock, n):
    for i in range(10):
        with lock:
            inc(n, 1)


if __name__ == "__main__":
    with mp.Manager() as manager:
        counter = manager.Value("i", 0)
        lock = manager.Lock()

        with ProcessPoolExecutor() as executor:
            executor.map(calculate, [lock, lock], [counter, counter])

        print(counter.value)
