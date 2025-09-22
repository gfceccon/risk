from abc import ABC

from risk.base.territory import TerritoryBase


class ContinentBase(ABC):
    name: str
    territories: list[TerritoryBase]

    def __init__(self, name: str, territories: list[TerritoryBase], bonus: int = 0):
        self.name = name
        self.territories = territories

    def reset(self) -> None:
        for territory in self.territories:
            territory.reset()

    def add_territories(self, territories: list[TerritoryBase]) -> None:
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
        result = f"==== {self.name} ===\n"
        if self.territories:
            result += f"{"\n".join([str(t) for t in self.territories])}"
        return result

    def __repr__(self) -> str:
        return f"{self.name} {" ".join([t.name for t in self.territories])}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ContinentBase):
            return False
        return self.name == value.name and self.territories == value.territories
