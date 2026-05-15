import asyncio
import random
from itertools_lib.stream_processor import DataStreamProcessor

async def log_file_simulator(lines_count: int):
    for i in range(lines_count):
        level = random.choice(["INFO", "ERROR", "DEBUG", "WARNING"])
        message = f"Подія номер {i}"
        yield f"[{level}] {message}"
        await asyncio.sleep(0.01)

async def run_demo():
    print("=== Початок інкрементальної обробки потоку даних ===")
    
    processor = DataStreamProcessor()
    
    raw_stream = log_file_simulator(100)
    
    processed_stream = processor.process_stream(
        stream=raw_stream,
        filter_func=lambda line: "[ERROR]" in line,
        transform=lambda line: f"ОБРОБЛЕНО: {line.upper()}"
    )

    count = 0
    async for result in processed_stream:
        print(result)
        count += 1
    
    print(f"\nОбробка завершена. Знайдено та оброблено {count} помилок.")

if __name__ == "__main__":
    asyncio.run(run_demo())