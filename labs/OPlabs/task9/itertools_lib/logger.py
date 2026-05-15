import time
import functools
import inspect
import datetime
from typing import Any, Callable, Optional

def log(level: str = "INFO", log_to_file: bool = False):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return execute_logging(func, level, log_to_file, *args, **kwargs)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            return await execute_logging(func, level, log_to_file, *args, **kwargs)

        return async_wrapper if inspect.iscoroutinefunction(func) else wrapper
    return decorator

def execute_logging(func, level, log_to_file, *args, **kwargs):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    func_name = func.__name__
    start_time = time.perf_counter()
    
    try:
        if inspect.iscoroutinefunction(func):
            result = yield from func(*args, **kwargs) 
        else:
            result = func(*args, **kwargs)
            
        execution_time = time.perf_counter() - start_time
        
        if level != "ERROR":
            log_msg = f"[{timestamp}] [{level}] Function '{func_name}' | Args: {args} {kwargs} | Result: {result} | Time: {execution_time:.4f}s"
            output_log(log_msg, log_to_file)
            
        return result
    except Exception as e:
        log_msg = f"[{timestamp}] [ERROR] Function '{func_name}' failed with error: {str(e)}"
        output_log(log_msg, log_to_file)
        raise e

def output_log(message: str, to_file: bool):
    print(message)
    if to_file:
        with open("app.log", "a", encoding="utf-8") as f:
            f.write(message + "\n")