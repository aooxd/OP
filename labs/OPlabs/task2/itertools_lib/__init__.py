import time
from typing import Generator, Any, Iterator

def fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def consume_with_timeout(iterator: Iterator[Any], timeout: float) -> Generator[Any, None, None]:
    """
    Итерирует объект, пока не истечет время timeout (в секундах).
    """
    if timeout < 0:
        raise ValueError("Timeout cannot be negative")
        
    start_time = time.time()
    for value in iterator:
        if time.time() - start_time >= timeout:
            break
        yield value