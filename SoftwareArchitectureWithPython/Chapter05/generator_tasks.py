import random
import time
import collections
import threading

def number_generator(n: int):
    """
    生成1到n之间数字的生成器
    :param n:
    :return:
    """
    for i in range(1, n+1):
        yield i

def square_mapper(numbers):
    """
    把数字转成其平方的生成器
    :param numbers:
    :return:
    """
    for n in numbers:
        yield n*n

def prime_filter(numbers):
    """
    过滤质数的生成器
    :param numbers:
    :return:
    """
    for n in numbers:
        if n%2 == 0:
            continue
        flag = True
        # 在奇数中筛选出: n>3时，质数无法被小于它的数整除
        for i in range(3, int(n**0.5+1),2):
            if n % i ==0:
                flag = False
                break
        if flag:
            yield n

def scheduler(tasks, runs=1000):
    """
    迭代逐个执行任务，将结果附加到使用函数名作为键的字典中，执行结束时返回字典
    :param tasks:
    :param runs:
    :return:
    """
    results = collections.defaultdict(list)
    for i in range(runs):
        for t in tasks:
            print("Switching to task", t.__name__)
            try:
                result = t.__next__()
                print("Result=>", result)
                results[t.__name__].append(result)
            except StopIteration:
                break
    return results

if __name__ == "__main__":
    import sys
    tasks = []
    # start = time.clock() # Python3.8不再支持time.clock(),但仍然可以调用
    start = time.perf_counter()
    limit = int(sys.argv[1])
    tasks.append(square_mapper(number_generator(limit)))
    tasks.append(prime_filter(number_generator(limit)))
    results = scheduler(tasks, runs=limit)
    print("Last prime=>", results['prime_filter'][-1])
    end = time.perf_counter()
    print(f"time taken=>{end-start}")
    # generator1 = number_generator(100)
    # print(generator1)
