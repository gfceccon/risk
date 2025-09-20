from risk.game.base.game_base import PlayerBase
from risk.game.base.game_base import StateBase


# TODO: Implement Reinforcement Learning Model


class RiskModel:
    def __init__(self):
        pass

    def predict(self, state: StateBase, player: PlayerBase) -> int:
        raise NotImplementedError()
