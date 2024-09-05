# Завантаження веб-сайтів з використанням багатопроцесорності
# Зверніть увагу на те скільки часу займає виконання цього скрипту і порівняйте з `./io_mt.py`
import time
import contextlib
import requests
from concurrent.futures import ProcessPoolExecutor, as_completed


@contextlib.contextmanager
def perf_time(title: str):
    start = time.perf_counter()
    yield
    print(f"{title} took {time.perf_counter() - start} seconds")


def download_site(url: str):
    with requests.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites: list[str]):
    with ProcessPoolExecutor() as executor:
        # ми більше не передаємо сессію, оскільки ми неможемо передати її між процесами
        # сессія повиина бути створена в кожному процесі окремо
        results = [executor.submit(download_site, url) for url in sites]
        list(as_completed(results))


def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    download_all_sites(sites)
    print(f"Downlaoded {len(sites)} in total")


if __name__ == "__main__":
    with perf_time("Main"):
        main()
