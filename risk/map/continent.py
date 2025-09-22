from risk.map.territory import Territory


class Continent:
    id: int
    name: str
    bonus: int
    territories: list[Territory]

    def __init__(self, id: int, name: str, territories: list[Territory], bonus: int = 0):
        self.id = id
        self.name = name
        self.bonus = bonus
        self.territories = territories

    def get_bonus(self) -> int:
        if all(t.owner is not None for t in self.territories):
            owners = {t.owner for t in self.territories}
            if len(owners) == 1:
                return self.bonus
        return 0

    def reset(self) -> None:
        for territory in self.territories:
            territory.reset()

    def add_territories(self, territories: list[Territory]) -> None:
        self.territories.extend(territories)

    def get_territory_by_name(self, name: str) -> Territory | None:
        filtered_territories = filter(
            lambda t: t.name == name, self.territories)
        return next(filtered_territories, None)

    def get_territory_by_number(self, number: int) -> Territory | None:
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
        if not isinstance(value, 'Continent'):
            return False
        return self.name == value.name and self.territories == value.territories
