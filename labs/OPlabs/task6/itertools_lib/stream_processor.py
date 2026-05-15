import asyncio
from typing import AsyncIterable, Callable, Any, TypeVar

T = TypeVar('T')
R = TypeVar('R')

class DataStreamProcessor:
    
    @staticmethod
    async def get_stream(data_source: AsyncIterable[T]) -> AsyncIterable[T]:
        async for item in data_source:
            yield item

    @staticmethod
    async def process_stream(
        stream: AsyncIterable[T], 
        transform: Callable[[T], R], 
        filter_func: Callable[[T], bool] = lambda x: True
    ) -> AsyncIterable[R]:
        async for item in stream:
            if filter_func(item):
                yield transform(item)