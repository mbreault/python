#!/usr/bin/env python3

## from https://docs.python.org/3/library/asyncio.html

import asyncio
import logging

async def squares(n):
    return (n,n**2)

def gather(n):
    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(*[squares(i) for i in range(n)])

    results = loop.run_until_complete(tasks)

    loop.close()

    print(results)

def main():
    n = 10
    gather(n)

if __name__ == '__main__':
     main()