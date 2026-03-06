from bisect import bisect_right


class Cache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.name = ""
        self.cache = []
    
    def request(self, x: int) -> bool:
        # this is an ABC so it should not actually be
        # instantiated
        raise NotImplementedError
    
    def __str__(self) -> str:
        return self.name


class FIFOCache(Cache):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        self.name = "FIFO"

    def request(self, x: int) -> bool:
        # --- hit ---
        if x in self.cache:
            return True
        # --- miss ---
        else: 
            if len(self.cache) >= self.capacity:
                self.cache.pop(0)
            self.cache.append(x)
            return False


class LRUCache(Cache):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        self.name = "LRU"

    def request(self, x: int) -> bool:
        if x in self.cache:
            self.cache.remove(x)
            self.cache.append(x)
            return True
        else:
            if len(self.cache) >= self.capacity:
                self.cache.pop(0)
            self.cache.append(x)
            return False


class OPTFFCache(Cache):
    def __init__(self, capacity: int, requests: list[int]):
        super().__init__(capacity)
        self.name = "OPTFF"
        self.requests = requests
        self.i = 0
        self.positions = {}
        for idx, val in enumerate(requests):
            self.positions.setdefault(val, []).append(idx)

    def _next_use(self, item: int, after_index: int) -> float:
        pos_list = self.positions.get(item, [])
        j = bisect_right(pos_list, after_index)
        if j >= len(pos_list):
            return float("inf")
        return pos_list[j]

    def request(self, x: int) -> bool:
        current_index = self.i
        self.i += 1

        if x in self.cache:
            return True
        else:
            if len(self.cache) < self.capacity:
                self.cache.append(x)
                return False

            evict_idx = 0
            farthest = -1.0

            for idx, item in enumerate(self.cache):
                nxt = self._next_use(item, current_index)
                if nxt > farthest:
                    farthest = nxt
                    evict_idx = idx

            self.cache.pop(evict_idx)
            self.cache.append(x)
            return False