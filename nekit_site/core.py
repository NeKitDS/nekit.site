from aiohttp import web
import gd

from .constants import port, routes
from .ext import *

app = gd.server.create_app()


async def run_async() -> None:
    app.add_routes(routes)
    await web._run_app(app, port=port)


def run() -> None:
    app.add_routes(routes)
    gd.server.run(app, port=port)
