from risk.game.base.territory_base import TerritoryBase
from risk.game.base.game_base import PlayerBase
from dataclasses import dataclass
import enum



class ActionEnum(enum.Enum):
    DEPLOY = 1
    ATTACK = 2
    FORTIFY = 3
    PASS_TURN = 4

@dataclass
class Action:
    action: ActionEnum
    player: PlayerBase
    num_units: int = 0

    target: PlayerBase | None = None

    territory_from: TerritoryBase | None = None
    territory_to: TerritoryBase | None = None