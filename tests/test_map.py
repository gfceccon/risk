from risk.game.map.world import World
from risk.game.map.territory import Territory
from risk.game.map.continent import Continent
import pytest

    
@pytest.mark.parametrize("attr,result", [
    ("territories", True),
    ("continents", True)
])
def test_map_has_attrs_at_init(game_map: World, attr: str, result: bool):
    assert hasattr(game_map, attr) == result
