import gd

from .constants import port, routes
from .ext import *

app = gd.server.create_app()


def run() -> None:
    app.add_routes(routes)
    gd.server.run(app, port=port)
