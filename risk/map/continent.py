from typing import List
from risk.base.continent_base import ContinentBase
from risk.base.territory_base import TerritoryBase


class Continent(ContinentBase):
    bonus_troops: int

    def __init__(self, name: str, territories: List[TerritoryBase], bonus_troops: int):
        super().__init__(name, territories)
        self.bonus_troops = bonus_troops