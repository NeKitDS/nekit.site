import os
from pathlib import Path

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

__all__ = ("static", "templates", "env", "routes", "port", "html_resp")

root = Path(__file__).parent

static = root / "static"
templates = static / "html"

env = Environment(loader=FileSystemLoader(templates), enable_async=True)

port = os.environ.get("PORT", 80)

routes = web.RouteTableDef()

routes.static("/static", static)


def html_resp(**kwargs) -> web.Response:
    kwargs.setdefault("content_type", "text/html")
    return web.Response(**kwargs)
