import asyncio
from itertools_lib.logger import log

@log(level="INFO")
def sync_add(a, b):
    return a + b

@log(level="DEBUG", log_to_file=True)
async def async_fetch_data():
    await asyncio.sleep(0.5)
    return {"status": "ok", "data": [10, 20]}

@log(level="ERROR")
def divide(a, b):
    return a / b

async def run_demo():
    print("=== Тестування Logging Decorator (Task 9) ===\n")
    
    sync_add(5, 10)
    
    await async_fetch_data()
    
    print("\n--- Тест помилки (ERROR level) ---")
    try:
        divide(10, 0)
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    asyncio.run(run_demo())