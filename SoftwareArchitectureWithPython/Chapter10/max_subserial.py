"""
代码计时和优化
1. 通过上下文管理器计算代码运行时间
"""
import time
from contextlib import contextmanager

# contextmanager装饰器将普通函数变为上下文管理器
@contextmanager
def timer():
    try:
        start = time.time()
        yield
    finally:
        end = (time.time()-start)*1000
        print(f"time taken {end} ms")
cases = (
    ([-5, 20, -10, 30, 15], 55),
)

import random
def num_array(size: int):
    """
    创建指定大小的随机数组
    :param size:
    :return:
    """
    nums = []
    for i in range(size):
        nums.append(random.randrange(-25, 30))
    return nums
def max_sum_subserial_v1(lst: list):
    """
    求最大连续子序列和
    空间复杂度O(n*n)，时间复杂度O(n*n)
    :param lst:
    :return:
    """
    print(__name__)

    sums = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sum_of_sub = sum(lst[i:j+1])
            # print(f"{lst[i:j+1]}=>{sum_of_sub}")
            sums.append(sum_of_sub)
    return max(sums)

def max_sum_subserial_v2(lst: list):
    """
    求最大子序列和, 优化版，空间复杂度O(1)
    :param lst:
    :return:
    """
    print(__name__)
    max_sum = 0
    sub = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sum_of_sub = sum(lst[i:j+1])
            if sum_of_sub > max_sum:
                max_sum = sum_of_sub
                sub = lst[i:j+1]
    return max_sum, sub

def max_sum_subserial_v3(lst: list):
    """
    优化版pro,时间复杂度O(n)，空间复杂度O(1)
    计算到从索引0到索引i为止的最大子序列和，数学归纳法
    从0到0的最大子序列和为:
    sum0 = max(0, lst[0])
    从0到1的最大子序列和为：
    sum1 = max(sum[0], sum[0]+lst[1])
    ...
    sumi = max(sum[i-1], sum[i-1]+lst[i])

    而最大子序列和则为max(sum0, sum1, ..., sumn
    :param lst:
    :return:
    """
    max_ending = 0
    max_so_far = 0
    for x in lst:
        max_ending = max(0, max_ending + x)
        max_so_far = max(max_ending, max_so_far)
    return max_so_far

if __name__ == "__main__":
    # for case in cases:
    #     with timer():
    #         result = max_sum_subserial_v1(case[0])
    #     print(result)
    #     assert result == case[1]
    #     with timer():
    #         max_sum, sub = max_sum_subserial_v2(case[0])
    #     print(max_sum, sub)
    #     assert max_sum == case[1]
    #
    with timer():
        test_arr = num_array(1000)
    with timer():
        print(max_sum_subserial_v1(test_arr))
    with timer():
        print(max_sum_subserial_v2(test_arr))
    with timer():
        print(max_sum_subserial_v3(test_arr))
