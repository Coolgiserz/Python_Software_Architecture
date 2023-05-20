from concurrent.futures import as_completed, ThreadPoolExecutor
import functools
import operator

def factorial(n):
    return functools.reduce(operator.mul, [i for i in range(1, n+1)])


# 在线程池中执行可调用操作
# executor接口提供两个方法：submit和map
# submit：提交一个可以异步执行的调用，返回一个表示可回调执行的future对象

with ThreadPoolExecutor(max_workers=3) as executor:
    future_map = {executor.submit(factorial, n): n for n in range(1,10)}
for future in as_completed(future_map):
    num = future_map[future]
    print(f"F of {num} is {future.result()}")