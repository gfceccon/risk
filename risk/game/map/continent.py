from typing import List
from risk.game.map.territory import Territory


class Continent:
    name: str
    territories: List[Territory]

    def __init__(self, name: str, territories: List[Territory]):
        self.name = name
        self.territories = territories

    def reset(self) -> None:
        for territory in self.territories:
            territory.reset()

    def get_territory_by_name(self, name: str) -> Territory | None:
        filtered_territories = filter(
            lambda t: t.name == name, self.territories)
        return next(filtered_territories, None)

    def get_territory_by_number(self, number: int) -> Territory | None:
        filtered_territories = filter(
            lambda t: t.id == number, self.territories)
        return next(filtered_territories, None)

    def __str__(self) -> str:
        return f"{self.name}({"|".join([str(t) for t in self.territories])})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Continent):
            return False
        return self.name == value.name and self.territories == value.territories
