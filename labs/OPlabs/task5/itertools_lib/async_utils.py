import asyncio
import threading
from typing import Callable, Any, List, Optional

class AbortController:
    def __init__(self):
        self.is_aborted = False

    def abort(self):
        self.is_aborted = True

async def async_map_promise(func: Callable, iterable: List[Any], controller: Optional[AbortController] = None) -> List[Any]:
    results = []
    for item in iterable:
        if controller and controller.is_aborted:
            print("--- Операцію перервано (Promise-based) ---")
            break
        results.append(await func(item))
    return results

def async_map_callback(func: Callable, iterable: List[Any], callback: Callable[[List[Any]], None], controller: Optional[AbortController] = None):
    def worker():
        results = []
        for item in iterable:
            if controller and controller.is_aborted:
                print("--- Операцію перервано (Callback-based) ---")
                break
            results.append(func(item))
        if not (controller and controller.is_aborted):
            callback(results)

    thread = threading.Thread(target=worker)
    thread.start()