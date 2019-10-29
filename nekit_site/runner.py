import os

from aiohttp import web
import gdapi

from .ext import *

routes = []

routes.append(web.get('/legacy_project/{query}', check_level))

routes.append(web.get('/', hello))

gdapi.app.add_routes(routes)

port = int(os.environ.get('PORT', 80))

def run():
    gdapi.run(port=port)
