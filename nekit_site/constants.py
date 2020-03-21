import os
from pathlib import Path

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

__all__ = ('css', 'templates', 'env', 'routes', 'port', 'html_resp')

root = Path(__file__).parent

css = root / 'css'
templates = root / 'templates'

env = Environment(loader=FileSystemLoader(templates))

port = os.environ.get('PORT', 80)

routes = web.RouteTableDef()


def html_resp(**kwargs) -> web.Response:
    kwargs.setdefault('content_type', 'text/html')
    return web.Response(**kwargs)
