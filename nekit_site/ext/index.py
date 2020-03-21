from ..constants import env, html_resp, routes, web

__all__ = ('handle_index',)

template = env.get_template('index.html')


@routes.get('/')
async def handle_index(request: web.Request) -> web.Response:
    return html_resp(text=template.render())
