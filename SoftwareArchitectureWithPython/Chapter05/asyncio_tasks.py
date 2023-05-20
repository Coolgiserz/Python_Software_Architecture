import asyncio

def number_generator(m, n):
    yield from range(m, n+1)

async def prime_filter(m, n):
    primes = []
    for i in number_generator(m, n):
        if i % 2 == 0:
            continue
        flag = True
        for j in range(3, int(i**0.5+1), 2):
            if i % j == 0:
                flag = False
                break
        if flag:
            print("Prime=>", i)
            primes.append(i)
        await asyncio.sleep(1.0)
    return tuple(primes)

async def square_mapper(m, n):
    squares = []
    for i in number_generator(m, n):
        print("Square=>", i*i)
        squares.append(i*i)
        # 把控制转交给其他协同例程
        await asyncio.sleep(1.0)
    return squares

def print_result(future):
    print("Result=>", future.result())
# 获取事件循环
loop = asyncio.get_event_loop()
# 建立future对象
future = asyncio.gather(prime_filter(10, 50), square_mapper(10, 50))
# 添加回调函数：一旦future对象执行完成，将自动调用
future.add_done_callback(print_result)
# 事件循环将一直运行到future对象完成执行
loop.run_until_complete(future)
loop.close()