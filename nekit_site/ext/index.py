from aiohttp import web

from ..constants import templates

__all__ = ('hello', 'index')


with open(templates/'index.html', 'r') as file:
    index = file.read()


async def hello(request):
    text = index % ('NeKitDS', 'The Site of NeKitDS')
    return web.Response(text=text, content_type='text/html')
