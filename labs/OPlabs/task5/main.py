import asyncio
import time
from itertools_lib.async_utils import async_map_promise, async_map_callback, AbortController

async def async_square(x):
    await asyncio.sleep(0.5)
    return x * x

def sync_square(x):
    time.sleep(0.5)
    return x * x

def my_callback(results):
    print(f"Результат з калбеку: {results}")

async def run_demo():
    data = [1, 2, 3, 4, 5]
    controller = AbortController()

    print("=== 1. Тест Callback-based (в окремому потоці) ===")
    async_map_callback(sync_square, data, my_callback)
    
    print("\n=== 2. Тест Async/Await (Promise-based) ===")
    results = await async_map_promise(async_square, data)
    print(f"Результат async/await: {results}")

    print("\n=== 3. Тест AbortController (Скасування) ===")
    new_controller = AbortController()
    
    task = asyncio.create_task(async_map_promise(async_square, data, new_controller))
    await asyncio.sleep(1)
    new_controller.abort()
    
    aborted_results = await task
    print(f"Частковий результат після скасування: {aborted_results}")

if __name__ == "__main__":
    asyncio.run(run_demo())