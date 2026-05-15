from typing import Callable, Dict, List, Any

class EventEmitter:
    def __init__(self):
        self._events: Dict[str, List[Callable]] = {}

    def subscribe(self, event_name: str, listener: Callable) -> Callable:
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(listener)
        
        return lambda: self.unsubscribe(event_name, listener)

    def unsubscribe(self, event_name: str, listener: Callable):
        if event_name in self._events:
            if listener in self._events[event_name]:
                self._events[event_name].remove(listener)

    def emit(self, event_name: str, data: Any = None):
        if event_name in self._events:
            for listener in self._events[event_name]:
                listener(data)