from risk.game.base.game_base import Action, PlayerAbstract
from risk.game.base.game_base import EvaluationFunctionAbstract, StateAbstract


# TODO: Implement Reinforcement Learning Model


class RiskModel:
    def __init__(self):
        pass

    def predict(self, state: StateAbstract, player: PlayerAbstract) -> Action:
        raise NotImplementedError()


# TODO: Implement Reinforcement Learning Evaluation Function


class RiskFunction(EvaluationFunctionAbstract):
    model: RiskModel

    def __init__(self, model: RiskModel):
        self.model = model

    def evaluate(self, state: StateAbstract, player: PlayerAbstract) -> Action:
        return self.model.predict(state, player)
