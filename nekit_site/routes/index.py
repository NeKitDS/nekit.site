from nekit_site.constants import env, html_resp, routes, web

__all__ = ("handle_index",)

template = env.get_template("index.html")

projects = [
    {
        "title": "gd.py",
        "info": (
            "gd.py is an API wrapper for Geometry Dash. "
            "It covers server, client and memory interaction in the game."
        ),
        "link": "https://github.com/NeKitDS/gd.py",
        "link_name": "GitHub",
    },
    {
        "title": "nekit.site",
        "info": "This is the project that focuses on creating this website.",
        "link": "https://github.com/NeKitDS/nekit.site",
        "link_name": "GitHub",
    }
]


@routes.get("/")
async def handle_index(request: web.Request) -> web.Response:
    text = await template.render_async(projects=projects)
    return html_resp(text=text)
