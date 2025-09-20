from typing import Dict, List, Sequence
from risk.game.base.game_base import PlayerBase, StateBase
from risk.game.base.game_base import Phase
from risk.game.base.map_base import MapBase


class State(StateBase):

    def __init__(self, players: List[PlayerBase], world: MapBase):
        super().__init__(players, world)

    def reset(self) -> None:
        super().reset()
        # TODO: Initialize the troops and territories for each player

    def legal_actions(self) -> list[int]:
        # TODO: Return the list of legal actions for the current player
        raise NotImplementedError

    def apply_action(self, action: int) -> None:
        # TODO: Apply the action to the game state
        raise NotImplementedError

    def is_terminal(self) -> bool:
        # TODO: Determine if the game state is terminal
        raise NotImplementedError

    def reward(self, player: PlayerBase) -> float:
        # TODO: Calculate the reward for the given player
        raise NotImplementedError

    def next_state(self) -> 'State':
        # TODO: Transition to the next state
        raise NotImplementedError

    def clone(self) -> 'State':
        # TODO: Return a deep copy of the current state
        raise NotImplementedError

    def observation_space(self, player: PlayerBase | None = None) -> Dict[str, object]:
        # TODO: Return the observation space for the given player
        raise NotImplementedError
