import time
import contextlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import batched


@contextlib.contextmanager
def perf_time(title: str):
    start = time.perf_counter()
    yield
    print(f"{title} took {time.perf_counter() - start} seconds")


def calc(n: int):
    sum([i * i for i in range(n)])


def calc_sums(numbers: list[int]):
    print(len(numbers))
    return [sum([i * i for i in range(n)]) for n in numbers]


def main():
    with ThreadPoolExecutor() as executor:
        futures = []
        for numbers in batched([5_000_000 + i for i in range(20)], 5):
            print(len(numbers))
            future = executor.submit(calc_sums, numbers)
            futures.append(future)
        list(as_completed(futures))


if __name__ == "__main__":
    with perf_time("Main"):
        main()
