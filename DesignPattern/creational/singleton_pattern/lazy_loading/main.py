# @Author: weirdgiser
# @Time: 2024/8/31
# @Function:
import json
import threading
from dataclasses import dataclass, asdict

@dataclass
class ConfigStruct:
    lesson: str
    name: str
    description: str
    type: str

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, "r") as fr:
            config_dict = json.load(fr)
        return cls(**config_dict)

class NonSingletonConfiguration:
    _config = None
    def __init__(self, config_dict):
        print(f"{threading.current_thread().name} creating config object")
        self._config = self._setup(config_dict)
        self.id = id(self)
    def __getattr__(self, item):
        if self._config is None:
            self._setup(None)
        return self._config.get(item, None)

    def _setup(self, config_dict: dict):
        if config_dict is None:
            config_dict = {}
        return config_dict


class SingletonConfiguration:
    _config = None

    def __new__(cls, **kwargs):
        if not cls._config:
            cls._config = super().__new__(cls)
        return cls._config

    def __init__(self, **kwargs):
        config_dict = kwargs.get("config_dict", None)
        thread_name = kwargs.get("name", threading.current_thread().name)
        print(f"{thread_name} init config object: {id(self)}")
        if config_dict is None:
            config_dict = {}
        self._config = config_dict


    def __getattr__(self, item):
        return self._config.get(item, None)


def create_singleton_worker(config_dict, name="T"):
    return SingletonConfiguration(config_dict=config_dict, name=name)


if __name__ == "__main__":
    from pathlib import Path
    config_dict = ConfigStruct.from_json(f"{Path(__file__).parent}/config.json")
    print(config_dict)
    print("懒汉单例模式-----")
    object_list = []
    for _ in range(10):
        object_list.append(SingletonConfiguration(config_dict=asdict(config_dict)))
    print(all(object_list[0] is obj for obj in object_list))
    print(object_list[0].lesson)

    print("非单例模式-----")
    c = NonSingletonConfiguration(asdict(config_dict))
    d = NonSingletonConfiguration(asdict(config_dict))
    print(c is d)
    print(c.lesson)

    print("单例模式---同一进程内多个线程创建的单例对象是同一个")
    threads = []
    for i in range(10):
        t = threading.Thread(target=create_singleton_worker, args=(asdict(config_dict), f"T{i}"))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()