from ast import Not


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
        raise NotImplementedError


class OPTFFCache(Cache):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        self.name = "OPTFF"

    def request(self, x: int) -> bool:
        raise NotImplementedError