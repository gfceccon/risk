from abc import ABC
import numpy as np
from risk.game.map.territory import Territory
from risk.game.map.continent import Continent


class Map(ABC):
    continents: dict[str, Continent]

    def __init__(self):
        self.continents = {}

    def reset(self) -> None:
        for continent in self.continents.values():
            continent.reset()

    def _create_borders(self, Borders: list[tuple[Territory, Territory]],
                        bidirectional: bool = True):
        for t1, t2 in Borders:
            t1.add_border(t2)
            if bidirectional:
                t2.add_border(t1)

    def to_matrix(self) -> np.ndarray:
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
                    raise ValueError(f"Territory {neighbor} not found in territory list.")
                matrix[i][j] = 1

        return np.array(matrix)
