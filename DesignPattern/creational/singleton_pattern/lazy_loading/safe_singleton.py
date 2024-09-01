# @Author: weirdgiser
# @Function: 对比线程安全的单例模式和线程不安全的单例模式
import threading
import time
thread_count = 200
create_count_safe = 0
create_count_unsafe = 0

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"cost time: {time.time()-start}")
    return wrapper
class UnSafeSingletonClass:
    _config = None

    def __new__(cls, **kwargs):
        global create_count_unsafe
        if not cls._config:
            print(f"{threading.current_thread().name} creating config object")
            create_count_unsafe += 1
            cls._config = super().__new__(cls)
        return cls._config

    def __init__(self):
        # print(f"{threading.current_thread().name} init config object: {id(self)}")
        pass


class SafeSingletonClass:
    _config = None
    _lock = threading.RLock()
    def __new__(cls, **kwargs):
        global create_count_safe
        with cls._lock:
            if not cls._config:
                print(f"{threading.current_thread().name} creating config object")
                create_count_safe += 1
                cls._config = super().__new__(cls)
        return cls._config

    def __init__(self):
        # print(f"{threading.current_thread().name} init config object: {id(self)}")
        pass


@timer
def test_safe():
    print("懒汉单例模式-----")
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=SafeSingletonClass, name=f"T{i}")
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(create_count_safe)

@timer
def test_unsafe():
    print("懒汉单例模式-----")
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=UnSafeSingletonClass, name=f"T{i}")
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(create_count_unsafe)



if __name__ == "__main__":
    test_safe()
    test_unsafe()