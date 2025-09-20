from typing import List
from risk.rl.model import RiskModel
from risk.base.player_base import PlayerBase

# TODO: Implement Reinforcement Learning Agent


class PlayerRL:
    model: RiskModel

    def __init__(self, name: str, id: int, model: RiskModel):
        self.model = model

    def reset(self) -> None:
        pass

    def pick(self, legal_actions: List[int]) -> int:
        pass

    def step(self, player: PlayerBase, action: int) -> None:
        pass
