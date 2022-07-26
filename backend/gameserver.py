import asyncio
import logging
from typing import Dict, List

from aiohttp import WSMsgType, web

from backend import schemas
from backend.player import Player
from backend.room import Room

logger = logging.getLogger(__name__)


class GameServer:
    """GameServer"""

    def __init__(self):
        self.rooms: Dict[str, Room] = {}
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
                await self.handle_message(player, message)
            elif msg.type == WSMsgType.ERROR:
                logger.error(f"ws connection closed with exception {ws.exception()}")

        logger.debug("closing connection")
        if player.roomid is not None:
            logger.debug(f"removing player {player.username} {player.id}")
            # remove player from his room
            await self.rooms[player.roomid].remove_player(player)
            if len(self.rooms[player.roomid].players) == 0:
                # delete empty room
                logger.debug(f"deleting room {player.roomid}")
                del self.rooms[player.roomid]
        self.players.remove(player)
        logger.debug("websocket connection closed")

        return ws

    async def server_loop(self):
        """Game server loop"""
        while True:
            for id, room in self.rooms.items():
                for player in room.players:
                    message = schemas.BaseMessage(
                        type="hello", content={"text": f"you're in room {id}"}
                    )
                    await player.ws.send_json(message.dict())
            await asyncio.sleep(1)

    async def handle_message(self, player: Player, message: schemas.BaseMessage):
        """Handle received messages"""
        if player.roomid is None and message.type == "joinRequest":
            # move to room view first
            response = schemas.BaseMessage(type="joinResponse", content={})
            await player.ws.send_json(response.dict())

            # then add player
            player.username = message.content["username"]
            player.roomid = message.content["roomid"]
            if message.content["roomid"] not in self.rooms:
                new_room = Room()
                self.rooms[message.content["roomid"]] = new_room

            await self.rooms[message.content["roomid"]].add_player(player)

        elif player.roomid is not None:
            await self.rooms[player.roomid].receive(player, message)
