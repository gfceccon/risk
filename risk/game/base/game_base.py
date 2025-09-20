from risk.game.base.config import Config
from risk.game.base.player_base import PlayerBase
from risk.game.base.map_base import MapBase
from typing import Dict, List, Sequence
from abc import ABC, abstractmethod
import enum


class Phase(enum.Enum):
    INITIALIZATION = 1
    DEPLOY = 2
    ATTACK = 3
    FORTIFY = 4
    GAME_OVER = 5


class StateBase(ABC):
    history: List[int]
    players: Sequence[PlayerBase]
    player_turn: PlayerBase
    world: MapBase
    phase: Phase

    def __init__(self, players: Sequence[PlayerBase], world: MapBase):
        self.phase = Phase.INITIALIZATION
        self.players = players
        self.world = world
        self.history = []

    @abstractmethod
    def reset(self) -> None:
        self.history = []
        self.phase = Phase.INITIALIZATION
        self.player_turn = self.players[0]
        self.world.reset()
        for player in self.players:
            player.reset()

    @abstractmethod
    def legal_actions(self) -> list[int]:
        raise NotImplementedError

    @abstractmethod
    def apply_action(self, action: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def is_terminal(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def reward(self, player: 'PlayerBase') -> float:
        raise NotImplementedError

    @abstractmethod
    def next_state(self) -> 'StateBase':
        raise NotImplementedError

    @abstractmethod
    def clone(self) -> 'StateBase':
        raise NotImplementedError

    @abstractmethod
    def observation_space(self, player: 'PlayerBase | None' = None) -> Dict[str, object]:
        raise NotImplementedError
