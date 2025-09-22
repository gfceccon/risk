import os
from risk.map.continent import Continent
from risk.map.territory import Territory
import numpy as np


class Map:
    continents: dict[str, Continent]

    def __init__(self):
        self.continents = {}

    def reset(self) -> None:
        for continent in self.continents.values():
            continent.reset()

    def add_borders(self, borders: list[tuple[Territory, Territory]]):
        for t1, t2 in borders:
            t1.add_border(t2)

    @classmethod
    def to_matrix(cls, game_map: 'Map') -> np.ndarray:
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
    def from_json(cls, file_name: str) -> 'Map':
        game_map = cls()
        file_path = os.path.join(os.path.dirname(__file__), 'maps', file_name)
        import json
        with open(file_path, 'r') as f:
            data = json.load(f)
        for continent_data in data["continents"]:
            continent = Continent(
                name=continent_data["name"],
                territories=[
                    Territory(name=territory["name"], id=territory["id"])
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

