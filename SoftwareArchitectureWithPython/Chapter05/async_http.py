import asyncio
import aiohttp
import async_timeout


async def fetch_page(session, url, timeout=60):
     with async_timeout.timeout(timeout):
        response = session.get(url)
        return response

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    urls = ("http://www.baidu.com",
        "http://www.google.com",
            "http://www.yahoo.com",
            "http://www.facebook.com",
            "http://www.reddit.com",
            "http://www.twitter.com")
    session = aiohttp.ClientSession(loop=loop)
    tasks = map(lambda x: fetch_page(session, x), urls)
    done, pending = loop.run_until_complete(asyncio.wait(tasks, timeout=120))
    loop.close()

    for future in done:
        response = future.result()
        print(response)
        response.close()
    # session.close()
    loop.close()
    # tasks = map(lambda x: print(x), urls)
    # # next(tasks)
    # while tasks:
    #     next(tasks)

