import logging
from typing import List

from backend.player import Player

logger = logging.getLogger(__name__)


class Room:
    """Room class"""

    def __init__(self):
        players: List[Player] = []  # noqa: F841
