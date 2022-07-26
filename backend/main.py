#!/usr/bin/env python3.10
import logging
import sys

from aiohttp import web

from backend.gameserver import GameServer

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


gameserver = GameServer()


async def start_background_tasks(app):
    """Create background tasks"""
    app["server_loop"] = app.loop.create_task(gameserver.server_loop())


def init_app(argv):
    """Initiate web application"""
    app = web.Application()
    app.add_routes([web.get("/ws", gameserver.websocket_handler)])
    app.on_startup.append(start_background_tasks)
    return app


if __name__ == "__main__":
    app = init_app(sys.argv)
    web.run_app(app)
