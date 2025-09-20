
from typing import List
from risk.base.player_base import PlayerBase


class PlayerRandom(PlayerBase):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)

    def reset(self) -> None:
        pass

    def pick(self, legal_actions: List[int]) -> int:
        import random
        return random.choice(legal_actions)

    def step(self, player: PlayerBase, action: int) -> None:
        pass
