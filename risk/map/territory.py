from typing import List
from risk.base.territory_base import TerritoryBase
from risk.map.border import Border


class Territory(TerritoryBase):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)

    def reset(self) -> None:
        self.owner = None
        self.num_units = 0
        for border in self.borders:
            border.reset()

    def add_borders(self, neighbors: List['TerritoryBase']):
        for neighbor in neighbors:
            if neighbor not in [b.destination for b in self.borders]:
                self.borders.append(Border(self, neighbor))
