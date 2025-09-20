from abc import ABC, abstractmethod
from typing import List


class TerritoryBase(ABC):
    name: str
    id: int
    borders: List['BorderBase']
    num_units: int
    owner: int | None

    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name
        self.borders = []
        self.owner = None
        self.num_units = 0

    @abstractmethod
    def reset(self) -> None:
        self.owner = None
        self.num_units = 0
        for border in self.borders:
            border.reset()

    @abstractmethod
    def add_borders(self, neighbors: List['TerritoryBase']):
        pass

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, TerritoryBase):
            return False
        return self.name == value.name and self.id == value.id

    def __str__(self) -> str:
        result = f"{self.id}.{self.name}"
        if self.borders:
            result += f"({" | ".join([str(n) for n in self.borders])})"
        return result

    def __repr__(self) -> str:
        return f"{self.id}.{self.name}"


class BorderBase(ABC):
    def __init__(self, origin: TerritoryBase, destination: TerritoryBase):
        self.origin = origin
        self.destination = destination

    def reset(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.origin} -> {self.destination}"

    def __repr__(self) -> str:
        return str(self)
