from typing import Dict, List, Tuple
from risk.base.continent_base import ContinentBase
from risk.base.territory_base import TerritoryBase
from abc import ABC
import numpy as np


class MapBase(ABC):
    continents: Dict[str, ContinentBase]

    def __init__(self):
        self.continents = {}

    def reset(self) -> None:
        for continent in self.continents.values():
            continent.reset()

    def _create_borders(self, Borders: list[tuple[TerritoryBase, TerritoryBase]],
                        bidirectional: bool = True):
        for t1, t2 in Borders:
            t1.add_borders([t2])
            if bidirectional:
                t2.add_borders([t1])

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
                    raise ValueError(
                        f"Territory {neighbor} not found in territory list.")
                matrix[i][j] = 1

        return np.array(matrix)

    def from_matrix(self, matrix: np.ndarray,
                    territory_names: List[Tuple[str, str]],
                    continent_bonus: Dict[str, int],
                    continent_impl: type[ContinentBase],
                    territory_impl: type[TerritoryBase],
                    border_impl: type[TerritoryBase]) -> None:

        for continent in self.continents.values():
            for territory in continent.territories:
                del territory
            del continent
        self.continents.clear()

        territory_dict = {
            name: border_impl(name, id)
            for id, (name, _) in enumerate(territory_names)
        }

        self.continents = {
            name: continent_impl(
                name, [territory_impl(name, id)],
                continent_bonus.get(name, 0))
            for id, (_, name) in enumerate(territory_names)
        }

        for i, (_, name) in enumerate(territory_names):
            territory1 = territory_dict[name]
            for j, (_, name2) in enumerate(territory_names):
                if matrix[i][j] == 1:
                    territory2 = territory_dict[name2]
                    territory1.add_borders([territory2])
