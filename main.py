import argparse
import os
from pathlib import Path

from src.cache import FIFOCache, LRUCache, OPTFFCache


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="data/data.in")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input path does not exist: {args.input}")
    else:
        print(f"Loading data from: {input_path}") 

    # --- read the inputs ---
    with open(input_path) as f:
        km = f.readline().rstrip()
        accesses = f.readline().rstrip()
        k, m = km.split(" ")
        k, m = int(k), int(m)
        accesses = [int(x) for x in accesses.split(" ")]
        print(f"k: {k}, m: {m}, accesses: {accesses}")
    
    FIFO_cache = FIFOCache(capacity=k)
    LRU_cache = LRUCache(capacity=k)
    OPTFF_cache = OPTFFCache(capacity=k)

    caches = [FIFO_cache, LRU_cache, OPTFF_cache]

    for cache in caches:
        num_misses = 0
        for access in accesses:
            if not cache.request(access):
                num_misses += 1
        print(f"{cache} : {num_misses}")




if __name__ == "__main__":
    main()
