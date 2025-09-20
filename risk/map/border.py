
from risk.base.territory_base import BorderBase, TerritoryBase


class Border(BorderBase):
    def __init__(self, origin: TerritoryBase, destination: TerritoryBase):
        super().__init__(origin, destination)

    def reset(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.origin} -> {self.destination}"

    def __repr__(self) -> str:
        return str(self)
