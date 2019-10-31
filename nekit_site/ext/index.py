from aiohttp import web

from ..constants import templates

__all__ = ('hello', 'index')


with open(templates/'index.html', 'r') as file:
    index = file.read()


async def hello(request):
    return web.Response(text=index, content_type='text/html')
