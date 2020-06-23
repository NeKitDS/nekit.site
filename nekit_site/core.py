from typing import Optional

from aiohttp import web
import gd

from nekit_site.constants import port, routes
from nekit_site.routes import *


def create_app(**kwargs) -> web.Application:
    app = gd.server.create_app(**kwargs)
    app.add_routes(routes)
    return app


async def run_async(app: Optional[web.Application] = None) -> None:
    if app is None:
        app = create_app()

    await web._run_app(app, port=port)


def run(app: Optional[web.Application] = None) -> None:
    if app is None:
        app = create_app()

    gd.server.run(app, port=port)
