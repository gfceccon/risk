from risk.game.base.game_base import PlayerAbstract
from risk.rl.model import RiskFunction, RiskModel

# TODO: Implement Reinforcement Learning Agent


class PlayerRL(PlayerAbstract):
    model: RiskModel

    def __init__(self, name, model: RiskModel):
        super().__init__(name, RiskFunction(model))
        self.model = model
