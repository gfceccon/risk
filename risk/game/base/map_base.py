from typing import Dict
from risk.game.base.config import Config, default_config
from risk.game.base.continent_base import ContinentBase
from risk.game.base.territory_base import TerritoryBase
from abc import ABC, abstractmethod
import numpy as np


class MapBase(ABC):
    continents: Dict[str, ContinentBase]
    config: Config

    def __init__(self, config: Config = default_config):
        self.continents = {}
        self.config = config
        
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
