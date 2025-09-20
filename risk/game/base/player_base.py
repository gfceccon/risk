
from abc import ABC, abstractmethod
from typing import List


class PlayerBase(ABC):
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def pick(self, legal_actions: List[int]) -> int:
        raise NotImplementedError

    @abstractmethod
    def step(self, player: 'PlayerBase', action: int) -> None:
        raise NotImplementedError
