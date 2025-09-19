from typing import List
from risk.game.base.game_base import PlayerAbstract


class Territory:
    name: str
    id: int
    borders: List['Border']
    num_units: int
    owner: PlayerAbstract | None

    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name
        self.borders = []
        self.owner = None
        self.num_units = 0

    def reset(self) -> None:
        self.owner = None
        self.num_units = 0
        for border in self.borders:
            border.reset()

    def add_border(self, neighbor: 'Territory'):
        if neighbor not in [b.destination for b in self.borders]:
            self.borders.append(Border(self, neighbor))

    def add_borders(self, neighbors: List['Territory']):
        for neighbor in neighbors:
            if neighbor not in [b.destination for b in self.borders]:
                self.borders.append(Border(self, neighbor))

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Territory):
            return False
        return self.name == value.name and self.id == value.id

    def __str__(self) -> str:
        return f"{self.id}.{self.name}"

    def __repr__(self) -> str:
        return str(self)
    
    def to_string(self) -> str:
        result = f"{self.id}.{self.name}"
        if self.borders:
            result += f"\nBorders\n{"|\n".join([str(n) for n in self.borders])}"
        return result


class Border:
    def __init__(self, origin: Territory, destination: Territory):
        self.origin = origin
        self.destination = destination

    def reset(self) -> None:
        # TODO: Reset any dynamic properties of the border if needed
        pass

    def __str__(self) -> str:
        return f"{self.origin} -> {self.destination}"
    
    def __repr__(self) -> str:
        return str(self)
