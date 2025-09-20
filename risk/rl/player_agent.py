from risk.game.base.game_base import PlayerBase
from risk.rl.model import RiskModel

# TODO: Implement Reinforcement Learning Agent


class PlayerRL(PlayerBase):
    model: RiskModel

    def __init__(self, name: str, id: int, model: RiskModel):
        super().__init__(name, id)
        self.model = model
