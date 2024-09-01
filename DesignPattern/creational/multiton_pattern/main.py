# @Author: weirdgiser
# @Time: 2024/9/1
# @Function:
import threading

_MAX_INSTANCE_LIMIT = 10
class MultitonClass:
    _instances = {}
    _max_instances = _MAX_INSTANCE_LIMIT
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        key = kwargs.get("name", threading.current_thread().native_id)
        if key not in cls._instances:
            with cls._lock:
                if key not in cls._instances:
                    if len(cls._instances) >= cls._max_instances:
                        raise Exception("Max instances limit reached")
                    cls._instances[key] = super().__new__(cls)
                    print(f"instance {key} created")
        return cls._instances[key]

if __name__ == "__main__":
    thread_count = 20
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=MultitonClass, kwargs={"name": f"thread-{i}"})
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    a1 = MultitonClass(name="thread-1")
    a2 = MultitonClass(name="thread-1")
    b1 = MultitonClass(name="thread-2")
    print(a1 is a2, a1 is b1)




