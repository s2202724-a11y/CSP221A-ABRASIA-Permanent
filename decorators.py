import functools
import logging

def log_action(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.info(f"[LOG] {self.name} is starting task: {func.__name__}")
        result = func(self, *args, **kwargs)
        logging.info(f"[LOG] {self.name} completed task: {func.__name__}")
        return result
    return wrapper