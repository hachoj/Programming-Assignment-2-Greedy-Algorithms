import argparse
import os
from pathlib import Path

from src.cache import FIFOCache, LRUCache, OPTFFCache


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str,default="data/data.in")
    parser.add_argument("-o", "--output", type=str, default="data/data.out")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input path does not exist: {args.input}")

    output_path = Path(args.output)
    misses_fifo = None
    misses_lru = None
    misses_optff = None
    if output_path.exists():
        with open(output_path) as f:
            misses_fifo = int(f.readline().rstrip())
            misses_lru = int(f.readline().rstrip())
            misses_optff = int(f.readline().rstrip())

    # --- read the inputs ---
    with open(input_path) as f:
        km = f.readline().rstrip()
        accesses = f.readline().rstrip()
        k, m = km.split(" ")
        k, m = int(k), int(m)
        accesses = [int(x) for x in accesses.split(" ")]
    

    
    FIFO_cache = FIFOCache(capacity=k)
    LRU_cache = LRUCache(capacity=k)
    OPTFF_cache = OPTFFCache(capacity=k, requests=accesses)

    caches = [FIFO_cache, LRU_cache, OPTFF_cache]

    for cache in caches:
        num_misses = 0
        for access in accesses:
            if not cache.request(access):
                num_misses += 1
        if (
            output_path.exists() and
            misses_fifo is not None and
            misses_lru is not None and
            misses_optff is not None
        ):
            if str(cache) == "FIFO":
                print(f"FIFO  : {num_misses}, should be: {misses_fifo}")
            elif str(cache) == "LRU":
                print(f"LRU   : {num_misses}, should be: {misses_lru}")
            else:
                print(f"OPTFF : {num_misses}, should be: {misses_optff}")
        else:
            if str(cache) == "FIFO":
                print(f"FIFO  : {num_misses}")
            elif str(cache) == "LRU":
                print(f"LRU   : {num_misses}")
            else:
                print(f"OPTFF : {num_misses}")


if __name__ == "__main__":
    main()