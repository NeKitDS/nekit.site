from nekit_site.constants import env, html_resp, routes, web

__all__ = ("handle_index",)

template = env.get_template("index.html")


@routes.get("/")
async def handle_index(request: web.Request) -> web.Response:
    text = await template.render_async()
    return html_resp(text=text)
