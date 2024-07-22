from typing import Callable, Any
from colorama import Fore, init
import time


class TerminalService:

    def __init__(self):
        init(autoreset=True)

    def exc_message(self, message: str, func: Callable, resp: str):
        print(Fore.LIGHTBLUE_EX + f'-Script: {message}')
        try:
            result = func()
            print(Fore.GREEN + f"{resp}")
            return result
        except Exception as e:
            raise e

    def time_exec(self, func: Callable) -> dict[str: float, str: Any]:
        start_time = time.time()
        result = func()
        end_time = time.time()
        runtime = round(float(end_time - start_time), 3)
        print(f"runtime: {str(round(runtime, 3))}")
        return {"runtime": str(runtime), "return": result}

    def time_exec_message(self, func, message, resp):
        timed_func = lambda: self.time_exec(func)
        result = self.exc_message(message, timed_func, resp)
        return result
