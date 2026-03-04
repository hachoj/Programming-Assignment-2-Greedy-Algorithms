import pytest

from cache import FIFOCache, LRUCache, OPTFFCache


def test_FIFO():
    k = 5
    m = 30
    accesses = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7]
    true_num_misses = 17

    cache = FIFOCache(k)
    num_misses = 0
    for access in accesses:
        if not cache.request(access):
            num_misses += 1
    assert num_misses == true_num_misses, f"Incorrect amount of misses: {num_misses} != {true_num_misses}."


def test_LRU():
    raise NotImplementedError

def test_OPTFF():
    raise NotImplementedError