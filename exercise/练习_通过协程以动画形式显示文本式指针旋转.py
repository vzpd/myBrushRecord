import asyncio
import itertools
import sys


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for chr in itertools.cycle('|/-\\'):
        status = chr + ' ' + msg
        write(status)
        flush()
        try:
            await asyncio.sleep(0.25)
        except asyncio.CancelledError:
            write('\x08' * len(status))
            break
        write('\x08' * len(status))


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.create_task(spin('thinking...'))
    res = await slow_function()
    spinner.cancel()
    return res


def main():
    print('begin')
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(supervisor())
    loop.close()
    print('done:', res)


if __name__ == '__main__':
    main()
