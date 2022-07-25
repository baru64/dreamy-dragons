import logging
from typing import List

from backend import schemas
from backend.player import Player

logger = logging.getLogger(__name__)


class Room:
    """Room class"""

    def __init__(self):
        self.players: List[Player] = []  # noqa: F841
        self.card = None

    async def add_player(self, player):
        """Add player to room"""
        # send current players to new player
        for p in self.players:
            add_message = schemas.BaseMessage(
                type="addPlayer", content={"id": p.id, "username": p.username}
            )
            await player.ws.send_json(add_message.dict())
        self.players.append(player)
        # send new player to all players
        for p in self.players:
            add_message = schemas.BaseMessage(
                type="addPlayer", content={"id": player.id, "username": player.username}
            )
            await p.ws.send_json(add_message.dict())

    async def remove_player(self, player):
        """Remove player from room"""
        self.players.remove(player)
        for p in self.players:
            remove_message = schemas.BaseMessage(
                type="removePlayer",
                content={"id": player.id, "username": player.username},
            )
            await p.ws.send_json(remove_message.dict())

    async def receive(self, player: Player, message: schemas.BaseMessage):
        """Handle room messages"""
        if self.card is None:
            # room view
            pass  # TODO handle start
        else:
            # TODO pass the message to the card logic
            pass
