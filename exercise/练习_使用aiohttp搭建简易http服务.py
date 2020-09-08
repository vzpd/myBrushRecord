import asyncio

from aiohttp import web


async def index(request):
    await asyncio.sleep(.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html', charset='utf-8')


async def hello(request):
    await asyncio.sleep(.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html', charset='utf-8')


async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8088)
    await site.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
