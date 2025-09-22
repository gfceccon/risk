from risk.base.territory import TerritoryBase, BorderBase


class Territory(TerritoryBase):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)

    def reset(self) -> None:
        self.owner = None
        self.num_units = 0
        for border in self.borders:
            border.reset()

    def add_border(self, neighbor: 'TerritoryBase'):
        if neighbor not in [b.destination for b in self.borders]:
            self.borders.append(Border(self, neighbor))

class Border(BorderBase):
    def __init__(self, origin: TerritoryBase, destination: TerritoryBase):
        super().__init__(origin, destination)

    def reset(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.origin.name} -> {self.destination.name}"

    def __repr__(self) -> str:
        return str(self)
