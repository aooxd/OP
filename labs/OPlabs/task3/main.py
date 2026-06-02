import time
from itertools_lib import memoize

@memoize(capacity=2, strategy="LRU")
def slow_func(n):
    print(f"--- Обчислюю для {n}... ---")
    time.sleep(1)
    return n * 10

def run_demo():
    print("1. Тест швидкості (LRU, ліміт 2):")
    print(f"Перший виклик (1): {slow_func(1)}")
    print(f"Повторний виклик (1): {slow_func(1)} (має бути миттєво)")
    
    print("\n2. Тест витіснення (LRU):")
    print(f"Виклик (2): {slow_func(2)}")
    print(f"Виклик (3): {slow_func(3)} (витіснить 1)")
    
    print("\n3. Перевірка: виклик (1) знову буде повільним (кеш очищено):")
    print(f"Виклик (1): {slow_func(1)}")

    @memoize(expiry=2)
    def timed_func(x):
        return x + 100

    print("\n4. Тест Time-Based Expiry (час життя 2 сек):")
    print(f"Результат: {timed_func(5)}")
    print("Чекаємо 3 секунди...")
    time.sleep(3)
    print("Виклик після паузи (результат буде обчислено заново):")
    print(f"Результат: {timed_func(5)}")

if __name__ == "__main__":
    run_demo()