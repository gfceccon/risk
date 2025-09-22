from .continent import Continent
from .territory import Territory
from .map import Map

world_map = Map.from_json('world.json')

__all__ = [
    "Continent",
    "Territory",
    "Map",
    "world_map"
]
