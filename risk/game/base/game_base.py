from risk.game.map.territory import Territory
from risk.game.base.game_base import PlayerAbstract
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List, Sequence
from risk.game.map.map import Map
import numpy as np
import enum

class StateAbstract(ABC):
    history: List['Action']
    players: Sequence['PlayerAbstract']
    player_turn: 'PlayerAbstract'
    world: Map
    phase: 'Phase'

    def __init__(self, players: Sequence['PlayerAbstract'], world: Map):
        assert len(
            players) >= 3, "There must be at least three players in the game."
        assert world.continents, "The world must have at least one continent."
        self.phase = Phase.INITIALIZATION
        self.players = players
        self.world = world
        self.history = []

    @abstractmethod
    def reset(self, num_troops: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def legal_actions(self) -> list['Action']:
        raise NotImplementedError

    @abstractmethod
    def apply_action(self, action: 'Action') -> None:
        raise NotImplementedError

    @abstractmethod
    def is_terminal(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def reward(self, player: 'PlayerAbstract') -> float:
        raise NotImplementedError

    @abstractmethod
    def next_state(self) -> 'StateAbstract':
        raise NotImplementedError

    @abstractmethod
    def clone(self) -> 'StateAbstract':
        raise NotImplementedError

    @abstractmethod
    def observation_space(self, player: 'PlayerAbstract | None' = None) -> 'Observation':
        raise NotImplementedError


class EvaluationFunctionAbstract(ABC):
    @abstractmethod
    def evaluate(self, state: StateAbstract, player: PlayerAbstract) -> 'Action':
        raise NotImplementedError

    def __call__(self, state: StateAbstract, player: PlayerAbstract) -> 'Action':
        return self.evaluate(state, player)


class PlayerAbstract(ABC):
    def __init__(self, name: str, function: 'EvaluationFunctionAbstract'):
        self.name = name
        self.function = function

    @abstractmethod
    def reset(self, game_state: StateAbstract) -> None:
        raise NotImplementedError

    @abstractmethod
    def step(self, game_state: StateAbstract) -> 'Action':
        raise NotImplementedError


class Phase(enum.Enum):
    INITIALIZATION = 1
    DEPLOY = 2
    ATTACK = 3
    FORTIFY = 4
    GAME_OVER = 5


class ActionEnum(enum.Enum):
    DEPLOY = 1
    ATTACK = 2
    FORTIFY = 3
    PASS_TURN = 4


@dataclass
class Action:
    action: ActionEnum
    player: PlayerAbstract
    num_units: int = 0

    target: PlayerAbstract | None = None

    territory_from: Territory | None = None
    territory_to: Territory | None = None


@dataclass
class Observation(ABC):
    player: PlayerAbstract
    state: dict[str, any]  # type: ignore

    @abstractmethod
    def from_state(self, state: StateAbstract) -> 'Observation':
        raise NotImplementedError
    
    @abstractmethod
    def to_state(self) -> StateAbstract:
        raise NotImplementedError
    
    @abstractmethod
    def tensor(self) -> np.ndarray:
        raise NotImplementedError
