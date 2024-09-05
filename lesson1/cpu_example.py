import time
import contextlib


@contextlib.contextmanager
def perf_time(title: str):
    start = time.perf_counter()
    yield
    print(f"{title} took {time.perf_counter() - start} seconds")


def calc(n: int):
    sum([i * i for i in range(n)])


def calc_sums(numbers: list[int]):
    return [sum([i * i for i in range(n)]) for n in numbers]


def main():
    numbers = [5_000_000 + i for i in range(20)]
    calc_sums(numbers)


if __name__ == "__main__":
    with perf_time("Main"):
        main()
