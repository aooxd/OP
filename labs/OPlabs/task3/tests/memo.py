import unittest
import time
from itertools_lib import memoize

class TestMemoization(unittest.TestCase):
    def test_basic_caching(self):
        calls = 0
        @memoize()
        def count_calls(x):
            nonlocal calls
            calls += 1
            return x

        count_calls(1)
        count_calls(1)
        self.assertEqual(calls, 1)

    def test_lru_eviction(self):
        @memoize(capacity=2, strategy="LRU")
        def func(x):
            return x
        
        func(1)
        func(2)
        func(3) 
        
        cache = func._cache.cache
        self.assertNotIn(((1,), ()), cache)
        self.assertIn(((3,), ()), cache)

if __name__ == "__main__":
    unittest.main()