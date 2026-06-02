import time
from collections import OrderedDict, Counter
from typing import Any, Callable, Dict, Optional, Tuple

class Cache:
    def __init__(self, capacity: Optional[int] = None, strategy: str = "LRU", expiry: Optional[float] = None, custom_policy: Optional[Callable] = None):
        self.cache: Dict[Any, Any] = OrderedDict() if strategy == "LRU" else {}
        self.capacity = capacity
        self.strategy = strategy
        self.expiry = expiry
        self.custom_policy = custom_policy
        
        self.access_count = Counter()  
        self.timestamps: Dict[Any, float] = {}  

    def _evict(self):
        if not self.cache:
            return

        if self.custom_policy:
            key_to_remove = self.custom_policy(self.cache)
            if key_to_remove in self.cache:
                self._remove(key_to_remove)
            return

        if self.strategy == "LRU":
            key, _ = next(iter(self.cache.items()))
            self._remove(key)

        elif self.strategy == "LFU":
            lfu_key = min(self.access_count, key=self.access_count.get)
            self._remove(lfu_key)

    def _remove(self, key: Any):
        self.cache.pop(key, None)
        self.access_count.pop(key, None)
        self.timestamps.pop(key, None)

    def get(self, key: Any) -> Optional[Any]:
        if key not in self.cache:
            return None

        if self.expiry and (time.time() - self.timestamps.get(key, 0) > self.expiry):
            self._remove(key)
            return None

        if self.strategy == "LRU" and isinstance(self.cache, OrderedDict):
            self.cache.move_to_end(key)
        
        self.access_count[key] += 1
        return self.cache[key]

    def set(self, key: Any, value: Any):
        if self.capacity and len(self.cache) >= self.capacity and key not in self.cache:
            self._evict()

        self.cache[key] = value
        self.timestamps[key] = time.time()
        self.access_count[key] = 1
        if self.strategy == "LRU" and isinstance(self.cache, OrderedDict):
            self.cache.move_to_end(key)

def memoize(capacity: Optional[int] = None, strategy: str = "LRU", expiry: Optional[float] = None, custom_policy: Optional[Callable] = None):
    cache_storage = Cache(capacity, strategy, expiry, custom_policy)

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            result = cache_storage.get(key)
            if result is None:
                result = func(*args, **kwargs)
                cache_storage.set(key, result)
            return result
        wrapper._cache = cache_storage
        return wrapper
    return decorator