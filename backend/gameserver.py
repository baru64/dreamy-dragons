import asyncio
import logging
from datetime import datetime
from typing import List

from aiohttp import WSMsgType, web

from backend import schemas
from backend.player import Player
from backend.room import Room

logger = logging.getLogger(__name__)


class GameServer:
    """GameServer"""

    def __init__(self):
        self.rooms: List[Room] = []
        self.players: List[Player] = []

    async def websocket_handler(self, request):
        """Main WebSocket handler"""
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        player = Player(ws)
        self.players.append(player)

        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                message = schemas.BaseMessage.parse_raw(msg.data)
                logger.debug(f"Received message: {message.dict()}")
            elif msg.type == WSMsgType.ERROR:
                logger.error(f"ws connection closed with exception {ws.exception()}")

        self.players.remove(player)
        logger.debug("websocket connection closed")

        return ws

    async def server_loop(self):
        """Game server loop"""
        while True:
            for player in self.players:
                message = schemas.BaseMessage(
                    type="hello",
                    content={"text": f"welcome! {datetime.now().isoformat()}"}
                )
                await player.ws.send_json(message.dict())
            await asyncio.sleep(0.01)
