from typing import Any, Optional, Tuple

class BiDirectionalPriorityQueue:
    def __init__(self):
        self._queue = []
        self._counter = 0

    def enqueue(self, item: Any, priority: int):
        self._queue.append({
            'item': item,
            'priority': priority,
            'index': self._counter
        })
        self._counter += 1

    def _get_element(self, mode: str, remove: bool = False) -> Any:
        if not self._queue:
            raise IndexError("Черга порожня")

        if mode == "highest":
            target = max(self._queue, key=lambda x: (x['priority'], -x['index']))
        elif mode == "lowest":
            target = min(self._queue, key=lambda x: (x['priority'], x['index']))
        elif mode == "oldest":
            target = min(self._queue, key=lambda x: x['index'])
        elif mode == "newest":
            target = max(self._queue, key=lambda x: x['index'])
        else:
            raise ValueError("Невірний режим")

        if remove:
            self._queue.remove(target)
        
        return target['item']

    def dequeue(self, mode: str = "highest") -> Any:
        return self._get_element(mode, remove=True)

    def peek(self, mode: str = "highest") -> Any:
        return self._get_element(mode, remove=False)

    def is_empty(self) -> bool:
        return len(self._queue) == 0