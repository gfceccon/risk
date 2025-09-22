from risk.rl.model import RiskModel
from risk.base.player import PlayerBase

# TODO: Implement Reinforcement Learning Agent


class PlayerRL(PlayerBase):
    model: RiskModel

    def __init__(self, name: str, id: int, model: RiskModel):
        self.model = model

    def reset(self) -> None:
        pass

    def pick(self, legal_actions: list[int]) -> int:
        return 0

    def step(self, player: PlayerBase, action: int) -> None:
        pass
