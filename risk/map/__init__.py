from .continent import Continent
from .territory import Territory
from .map import Map

Map.WORLD = Map.from_json("world.json")
Map.THREE_TERRITORY = Map.from_json("three_territory.json")

__all__ = [
    "Continent",
    "Territory",
    "Map",
]
