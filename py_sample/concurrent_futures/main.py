import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from unicodedata import normalize
from time import time


def encode(text: str) -> str:
    t = text.lower()
    t = normalize("NFKC", t)
    t = text.upper()
    t = text.replace("a", "b")
    return t


async def aencode(text: str) -> str:
    t = text.lower()
    t = normalize("NFKC", t)
    t = text.upper()
    t = text.replace("a", "b")
    return t


def base(text: str, n_trial: int=100000):
    for _ in range(n_trial):
        _ = encode(text)


async def abase(text: str, n_trial: int=100000):
    for _ in range(n_trial):
        _ = await aencode(text)


def fast(text: str, n_worker: int = 10, n_trial: int=100000):
    with ProcessPoolExecutor(n_worker) as executer:
        futures = {executer.submit(encode, str(text)): i for i in range(n_trial)}
        for future in as_completed(futures):
            _ = future.result()


def slow(text: str, n_worker: int = 10, n_trial: int=100000):
     with ProcessPoolExecutor(n_worker) as executer:
        futures = {executer.submit(encode, text): i for i in range(n_trial)}
        for future in as_completed(futures):
            _ = future.result()


def tfast(text: str, n_worker: int = 10, n_trial: int=100000):
    with ThreadPoolExecutor(n_worker) as executer:
        futures = {executer.submit(encode, str(text)): i for i in range(n_trial)}
        for future in as_completed(futures):
            _ = future.result()


def tslow(text: str, n_worker: int = 10, n_trial: int=100000):
     with ThreadPoolExecutor(n_worker) as executer:
        futures = {executer.submit(encode, text): i for i in range(n_trial)}
        for future in as_completed(futures):
            _ = future.result()


def main():
    text = "hello, world!"
    start = time()
    fast(text)
    end = time()
    print(f"pfast: {end - start}")
    
    start = time()
    slow(text)
    end = time()
    print(f"pslow: {end - start}")

    start = time()
    tfast(text)
    end = time()
    print(f"tfast: {end - start}")
    
    start = time()
    tslow(text)
    end = time()
    print(f"tslow: {end - start}")

    start = time()
    base(text)
    end = time()
    print(f"base : {end - start}")

    start = time()
    asyncio.run(abase(text))
    end = time()
    print(f"abase: {end - start}")
    print()

    print("DONE")


if __name__ == "__main__":
    main()
