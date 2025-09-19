
import pytest
from risk.game.map.map import Map
from risk.game.map.territory import Territory
from risk.game.map.continent import Continent
from risk.game.map.world import World

@pytest.fixture
def game_map() -> Map:
    game_map = Map()
    return game_map