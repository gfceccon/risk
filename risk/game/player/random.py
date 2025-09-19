

from risk.game.base.game_base import Action
from risk.game.base.game_base import PlayerAbstract, EvaluationFunctionAbstract, StateAbstract


class RandomFunction(EvaluationFunctionAbstract):
    def evaluate(self, state: StateAbstract, player: PlayerAbstract) -> Action:
        import random
        actions = state.legal_actions()
        if not actions:
            raise ValueError("No legal actions available")
        return random.choice(actions)

    def __call__(self, state: StateAbstract, player: PlayerAbstract) -> Action:
        return self.evaluate(state, player)


class PlayerRandom(PlayerAbstract):
    id: int
    name: str
    function: EvaluationFunctionAbstract

    def __init__(self, id: int, name: str, function: EvaluationFunctionAbstract = RandomFunction()):
        self.id = id
        self.name = name
        self.function = function

    def reset(self, game_state: StateAbstract) -> None:
        pass

    def step(self, game_state: StateAbstract) -> Action:
        return self.function(game_state, self)
