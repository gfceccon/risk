from abc import ABC
from typing import List

from risk.base.territory_base import TerritoryBase


class ContinentBase(ABC):
    name: str
    territories: List[TerritoryBase]

    def __init__(self, name: str, territories: List[TerritoryBase], bonus: int = 0):
        self.name = name
        self.territories = territories

    def reset(self) -> None:
        for territory in self.territories:
            territory.reset()

    def add_territories(self, territories: List[TerritoryBase]) -> None:
        self.territories.extend(territories)

    def get_territory_by_name(self, name: str) -> TerritoryBase | None:
        filtered_territories = filter(
            lambda t: t.name == name, self.territories)
        return next(filtered_territories, None)

    def get_territory_by_number(self, number: int) -> TerritoryBase | None:
        filtered_territories = filter(
            lambda t: t.id == number, self.territories)
        return next(filtered_territories, None)

    def __str__(self) -> str:
        return f"{self.name}({"|".join([str(t) for t in self.territories])})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ContinentBase):
            return False
        return self.name == value.name and self.territories == value.territories
