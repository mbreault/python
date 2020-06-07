#!/usr/bin/env python3

## from https://docs.python.org/3/library/asyncio.html

import asyncio
import logging

async def main():
    logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.INFO)
    logging.info('Hello ...')
    await asyncio.sleep(1)
    logging.info('... World!')

# Python 3.7+
if __name__ == '__main__':
    asyncio.run(main())