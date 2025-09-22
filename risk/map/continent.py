from risk.base.continent import ContinentBase
from risk.base.territory import TerritoryBase


class Continent(ContinentBase):
    def __init__(self, name: str, territories: list[TerritoryBase], bonus: int):
        super().__init__(name, territories, bonus)