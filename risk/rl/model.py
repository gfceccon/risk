from risk.base.player import PlayerBase
from risk.risk import RiskState


# TODO: Implement Reinforcement Learning Model


class RiskModel:
    def __init__(self):
        pass

    def predict(self, state: RiskState, player: PlayerBase) -> int:
        raise NotImplementedError()
