def calc(n: int):
    sum([i * i for i in range(n)])


def calc_sums(numbers: list[int]):
    return [sum([i * i for i in range(n)]) for n in numbers]


def do_calc():
    numbers = [5_000_000 + i for i in range(20)]
    return calc_sums(numbers)
