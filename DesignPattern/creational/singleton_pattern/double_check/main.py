import threading
import time
thread_count = 200
create_count_doublecheck = 0


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"cost time: {time.time()-start}")
    return wrapper

class SafeDoubleCheckSingletonClass:
    _config = None
    _lock = threading.RLock()
    def __new__(cls, **kwargs):
        global create_count_doublecheck
        if not cls._config:
            with cls._lock:
                if not cls._config:
                    print(f"{threading.current_thread().name} creating config object")
                    create_count_doublecheck += 1
                    cls._config = super().__new__(cls)
        return cls._config

@timer
def test_safe_doublecheck():
    print("双重检测单例-----")
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=SafeDoubleCheckSingletonClass, name=f"T{i}")
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(create_count_doublecheck)


if __name__ == "__main__":
    test_safe_doublecheck()