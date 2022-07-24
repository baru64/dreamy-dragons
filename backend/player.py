import logging

from aiohttp import web

logger = logging.getLogger(__name__)


class Player:
    """Player class"""

    def __init__(self, ws: web.WebSocketResponse):
        self.ws = ws
