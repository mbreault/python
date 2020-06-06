#!/usr/bin/env python3

## from https://docs.python.org/3/library/asyncio.html

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())