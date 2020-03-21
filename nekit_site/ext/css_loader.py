from ..constants import css, routes, web

__all__ = ('res_map', 'handle_css')

res_map = {
    file.name: file.read_text('utf-8') for file in css.iterdir()
}

@routes.get('/css/{name}')
async def handle_css(request: web.Request) -> web.Response:
    data = res_map.get(request.match_info.get('name'))

    if data is None:
        raise web.HTTPNotFound()

    return web.Response(text=data, content_type='text/css')
