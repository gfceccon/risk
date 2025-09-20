from dataclasses import dataclass, field
from abc import ABC
from typing import Dict


@dataclass
class Config:
    INITIAL_TROOPS: Dict[int, int] = field(
        default_factory=lambda: {
            3: 35,
            4: 30,
            5: 25,
            6: 20,
        })
    MIN_PLAYERS: int = 3
    MAX_PLAYERS: int = 6
    MAX_TURNS: int = 1000
    MAX_ATTACK_DICE: int = 3
    MAX_DEFEND_DICE: int = 2
    CONTINENT_BONUSES: Dict[str, int] = field(
        default_factory=lambda: {
            "north_america": 1,
            "south_america": 1,
            "europe": 1,
            "africa": 1,
            "asia": 1,
            "australia": 1,
        })


default_config = Config()
