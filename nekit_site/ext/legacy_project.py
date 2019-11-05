from aiohttp import web

from gdapi.utils import json_resp
import gdapi

LEGACY_PASTEBIN = 'https://pastebin.com/raw/VXKF1KtN'

gd, client = gdapi.gd, gdapi.client

__all__ = ('LEGACY_PASTEBIN', 'check_level')


async def check_level(request):
    req = request.match_info.get('query')

    try:
        query = int(req)

    except ValueError:
        return web.Response(
            text='Expected query of type <int>, got {!r}.'.format(req), status=503
        )

    try:
        level = await client.get_level(query)
    except gd.GDException:
        return web.Response(text='Level with ID {} was not found.'.format(query), status=404)

    categories = ('reserved_ok', 'in_pack_or_world_ok', 'rated_ok')
    approved = [True, True, True]

    params = request.rel_url.query

    accept_reserved = int(params.get('accept_reserved', 0))

    if not accept_reserved:
        try:
            resp = await gd.http.normal_request(LEGACY_PASTEBIN)
            data = await resp.content.read()
            text = data.decode()

        except Exception:
            return web.Response(text='Failed to fetch creator list for checking.', status=404)

        creators = [name.lstrip('- ') for name in text.split('\r\n')]

        approved[0] = (level.creator.name not in creators)

    allow_world_or_packs = int(params.get('allow_world_or_packs', 0))

    if not allow_world_or_packs:
        try:
            filters = gd.Filters(strategy='world')
            world_levels, map_packs, gauntlets = (
                await client.search_levels(pages=range(100), filters=filters),
                await client.get_map_packs(pages=range(100)),
                await client.get_gauntlets()
            )

        except gd.GDException:
            return web.Response(text='Failed to load required data to compare against the level.', status=404)

        check_against = [level.id for level in world_levels]

        for map_pack in map_packs:
            check_against.extend(map_pack.level_ids)

        for gauntlet in gauntlets:
            check_against.extend(gauntlet.level_ids)

        approved[1] = (level.id not in check_against)

    rate_status = int(params.get('rate_status', 2))

    rate_map = {
        0: True, 1: level.is_rated(), 2: level.is_featured(), 3: level.is_epic()
    }

    approved[2] = rate_map.get(rate_status, False)

    verified, detailed = all(approved), dict(zip(categories, approved))

    info = gdapi.make_level_dict(level)

    final = {'approved': verified, 'analysis': detailed, **info}

    return json_resp(final)
