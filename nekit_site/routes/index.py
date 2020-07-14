from datetime import datetime

from nekit_site.constants import env, html_resp, routes, web

__all__ = ("handle_index",)

template = env.get_template("index.html")

projects = [
    {
        "title": "nekit.site",
        "info": "This is the project that focuses on creating this website.",
        "links": [
            {
                "url": "https://github.com/NeKitDS/nekit.site",
                "name": "GitHub",
            }
        ]
    },
    {
        "title": "enums.py",
        "info": "Enhanced Enum Implementation for Python.",
        "links": [
            {
                "url": "https://github.com/NeKitDS/enums.py",
                "name": "GitHub",
            }
        ]
    },
    {
        "title": "gd.py",
        "info": (
            "gd.py is an API wrapper for Geometry Dash. "
            "It covers server, client and memory interaction in the game."
        ),
        "links": [
            {
                "url": "https://github.com/NeKitDS/gd.py",
                "name": "GitHub",
            }
        ]
    },
    {
        "title": "gd.rpc",
        "info": "gd.rpc implements Discord Rich Presence for Geometry Dash.",
        "links": [
            {
                "url": "https://github.com/NeKitDS/gd.rpc",
                "name": "GitHub",
            },
            {
                "url": "https://www.youtube.com/watch?v=A5NDM6ZIjYE",
                "name": "YouTube",
            }
        ]
    }
]


@routes.get("/")
async def handle_index(request: web.Request) -> web.Response:
    age = datetime.utcnow().year - 2004  # hehe

    text = await template.render_async(age=age, projects=projects)

    return html_resp(text=text)
