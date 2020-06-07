#!/usr/bin/env python3

## from https://docs.python.org/3/library/asyncio.html

import asyncio
import logging

async def squares(n):
    return (n,n**2)

def wait(n):
    loop = asyncio.get_event_loop()
    tasks = [squares(i) for i in range(n)]

    results, _ = loop.run_until_complete(asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED))

    loop.close()

    for result in results:
        print(result.result())

def gather(n):
    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(*[squares(i) for i in range(n)])

    results = loop.run_until_complete(tasks)

    loop.close()

    print(results)

def main():
    n = 10
    wait(n)
    #gather(n)

# Python 3.7+
if __name__ == '__main__':
     main()