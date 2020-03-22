from ..constants import routes, web

import gd

client = gd.server.CLIENT
LEGACY_PASTEBIN = 'https://pastebin.com/raw/VXKF1KtN'

__all__ = ('LEGACY_PASTEBIN', 'check_level')


class Handler:
    world_levels = ()
    map_packs = ()
    gauntlets = ()
    creators = ()


@gd.tasks.loop(seconds=30)
async def loader():
    try:
        Handler.world_levels = (
            await client.search_levels(pages=range(100), filters=gd.Filters(strategy='world'))
        )
        Handler.map_packs = await client.get_map_packs(pages=range(100))
        Handler.gauntlets = await client.get_gauntlets()

        async with client.http.normal_request(LEGACY_PASTEBIN) as pastebin:
            data = await pastebin.content.read()

        Handler.creators = [name.lstrip('- ') for name in data.decode().split('\r\n')]

    except Exception:
        pass  # uwu

loader.start()


@routes.get('/legacy_project/{query}')
@gd.server.handle_errors({
    ValueError: gd.server.Error(400, 'Invalid type in payload.'),
    gd.MissingAccess: gd.server.Error(404, 'Requested level was not found.')
})
async def check_level(request: web.Request) -> web.Response:
    query = int(request.match_info.get('query'))
    params = request.rel_url.query

    level = await client.get_level(query)

    checks = ('reserved_ok', 'world_or_packs_ok', 'rate_status_ok')
    analysis = []

    if not gd.server.str_to_bool(params.get('accept_reserved', 'false')):
        analysis.append(level.creator.name not in Handler.creators)

    if not gd.server.str_to_bool(params.get('allow_world_or_packs', 'false')):
        check_against = [level.id for level in Handler.world_levels]

        for map_pack in Handler.map_packs:
            check_against.extend(map_pack.level_ids)

        for gauntlet in Handler.gauntlets:
            check_against.extend(gauntlet.level_ids)

        analysis.append(level.id not in check_against)

    rate_map = {
        0: True, 1: level.is_rated(), 2: level.is_featured(), 3: level.is_epic()
    }

    analysis.append(rate_map.get(int(params.get('rate_status', 2))))

    verified, detailed = all(analysis), dict(zip(checks, analysis))

    final = {'approved': verified, 'analysis': detailed, 'data': level}

    return gd.server.json_resp(final)
