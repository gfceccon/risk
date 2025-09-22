

class Territory:
    id: int
    name: str
    borders: list['Border']
    owner: int | None
    num_units: int
    continent_id: int

    def __init__(self, id: int, name: str, continent_id: int):
        self.id = id
        self.name = name
        self.borders = []
        self.owner = None
        self.num_units = 0
        self.continent_id = continent_id

    def reset(self) -> None:
        self.owner = None
        self.num_units = 0
        for border in self.borders:
            border.reset()

    def add_border(self, neighbor: 'Territory') -> None:
        if neighbor not in [b.destination for b in self.borders]:
            self.borders.append(Border(self, neighbor))

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, type(Territory)):
            return False
        return self.name == value.name and self.id == value.id

    def __str__(self) -> str:
        result = f"{self.id}.{self.name}\n"
        if self.borders:
            result += f"---> {"\n---> ".join([f"{n.destination.name}" for n in self.borders])}"
        return result

    def __repr__(self) -> str:
        return f"{self.id}.{self.name}"


class Border:
    def __init__(self, origin: Territory, destination: Territory):
        self.origin = origin
        self.destination = destination

    def reset(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.origin.name} -> {self.destination.name}"

    def __repr__(self) -> str:
        return str(self)
