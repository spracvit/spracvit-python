import time
import logging


def measure(func):
    """
    Decorate a function to log how much time the function call took
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_taken = time.perf_counter() - start
        logging.info(f"Function {func.__name__} took {time_taken}s")
        return result
    return wrapper


def repeat(n):
    """
    Decorate a function to run it `n` times
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator
