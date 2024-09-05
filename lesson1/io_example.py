import time
import contextlib
import requests


@contextlib.contextmanager
def perf_time(title: str):
    start = time.perf_counter()
    yield
    print(f"{title} took {time.perf_counter() - start} seconds")


def download_site(session: requests.Session, url: str):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites: list[str]):
    with requests.Session() as session:
        for url in sites:
            download_site(session, url)


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
