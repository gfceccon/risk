from risk.base.continent import ContinentBase
from risk.base.territory import TerritoryBase
from abc import ABC, abstractmethod
import numpy as np


class MapBase(ABC):
    continents: dict[str, ContinentBase]

    def __init__(self):
        self.continents = {}

    @abstractmethod
    def reset(self) -> None:
        for continent in self.continents.values():
            continent.reset()

    @abstractmethod
    def add_borders(self, borders: list[tuple[TerritoryBase, TerritoryBase]]):
        for t1, t2 in borders:
            t1.add_border(t2)

    @classmethod
    def to_matrix(cls, game_map: 'MapBase') -> np.ndarray:
        self = game_map
        territory_list = [
            territory for continent in self.continents.values()
            for territory in continent.territories
        ]
        territory_dict = {
            str(territory): idx for idx, territory in enumerate(territory_list)
        }
        size = len(territory_dict)
        matrix = [[0] * size for _ in range(size)]

        for i, territory in enumerate(territory_list):
            for neighbor in territory.borders:
                j = territory_dict.setdefault(str(neighbor), -1)
                if j == -1:
                    continue
                matrix[i][j] = 1

        return np.array(matrix)

    @classmethod
    def from_json(cls, file_name: str,
                  continent_impl: type[ContinentBase],
                  territory_impl: type[TerritoryBase]) -> 'MapBase':
        game_map = cls()
        import json
        with open(file_name, 'r') as f:
            data = json.load(f)
        for continent_data in data["continents"]:
            continent = continent_impl(
                name=continent_data["name"],
                territories=[
                    territory_impl(name=territory["name"], id=territory["id"])
                    for territory in continent_data["territories"]
                ],
                bonus=continent_data["bonus"]
            )
            game_map.continents[continent.name] = continent
        borders = []
        for continent_data in data["continents"]:
            continent = game_map.continents[continent_data["name"]]
            for territory_data in continent_data["territories"]:
                territory = next(
                    t for t in continent.territories
                    if t.name == territory_data["name"])
                for neighbor_name in territory_data["borders"]:
                    neighbor = continent.get_territory_by_name(neighbor_name)
                    if neighbor:
                        borders.append((territory, neighbor))
        game_map.add_borders(borders)
        return game_map

    def __str__(self) -> str:
        result = ""
        for continent in self.continents.values():
            result += f"{continent}\n"
        return result

if __name__ == "__main__":
    from risk.map.continent import Continent
    from risk.map.territory import Territory

    class TestMap(MapBase):
        def reset(self) -> None:
            super().reset()
        def add_borders(self, borders: list[tuple[TerritoryBase, TerritoryBase]]):
            super().add_borders(borders)

    test_map = TestMap.from_json(
        "world.json", Continent, Territory)
    print("Successfully loaded map from JSON")
    print(test_map)