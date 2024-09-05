import multiprocessing as mp


def inc(counter, value=1):
    with counter.get_lock():
        counter.value += value


def calculate(n):
    for i in range(10):
        inc(n, 1)


if __name__ == "__main__":
    value = mp.Value("i", 0)
    p = [
        mp.Process(target=calculate, args=(value,)),
        mp.Process(target=calculate, args=(value,)),
    ]
    for i in p:
        i.start()
    for i in p:
        i.join()

    print(value.value)
