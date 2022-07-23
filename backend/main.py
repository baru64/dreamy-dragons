#!/usr/bin/env python3.10
import asyncio
import logging
import sys
from datetime import datetime
from typing import List

from aiohttp import WSMsgType, web

from backend import schemas

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

websockets: List[web.WebSocketResponse] = []


async def websocket_handler(request):
    """Main WebSocket handler"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    websockets.append(ws)

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            message = schemas.BaseMessage.parse_raw(msg.data)
            logger.debug(f"Received message: {message.dict()}")
        elif msg.type == WSMsgType.ERROR:
            logger.error(f"ws connection closed with exception {ws.exception()}")

    websockets.remove(ws)
    logger.debug("websocket connection closed")

    return ws


async def server_loop():
    """Game server loop"""
    while True:
        for ws in websockets:
            message = schemas.BaseMessage(
                type="hello",
                content=f"welcome! {datetime.now().isoformat()}"
            )
            await ws.send_json(message.dict())
        await asyncio.sleep(0.01)


async def start_background_tasks(app):
    """Create background tasks"""
    app["server_loop"] = app.loop.create_task(server_loop())


def init_app(argv):
    """Initiate web application"""
    app = web.Application()
    app.add_routes([web.get("/ws", websocket_handler)])
    app.on_startup.append(start_background_tasks)
    return app


if __name__ == "__main__":
    app = init_app(sys.argv)
    web.run_app(app)
