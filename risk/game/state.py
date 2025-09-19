from typing import List, Sequence
from risk.game.base.game_base import PlayerAbstract, StateAbstract
from risk.game.base.game_base import Action, Phase, Observation
from risk.game.map.map import Map
from risk.game.map.world import World


class State(StateAbstract):

    def __init__(self, players: List[PlayerAbstract], world: Map):
        super().__init__(players, world)

    def reset(self, num_troops: int) -> None:
        self.history = []
        self.phase = Phase.INITIALIZATION
        self.player_turn = self.players[0]
        self.world.reset()
        for player in self.players:
            player.reset(self)
        # TODO: Initialize the troops and territories for each player

    def legal_actions(self) -> list[Action]:
        # TODO: Return the list of legal actions for the current player
        raise NotImplementedError

    def apply_action(self, action: Action) -> None:
        # TODO: Apply the action to the game state
        raise NotImplementedError

    def is_terminal(self) -> bool:
        # TODO: Determine if the game state is terminal
        raise NotImplementedError

    def reward(self, player: PlayerAbstract) -> float:
        # TODO: Calculate the reward for the given player
        raise NotImplementedError

    def next_state(self) -> 'State':
        # TODO: Transition to the next state
        raise NotImplementedError

    def clone(self) -> 'State':
        # TODO: Return a deep copy of the current state
        raise NotImplementedError

    def observation_space(self, player: PlayerAbstract | None = None) -> Observation:
        # TODO: Return the observation space for the given player
        raise NotImplementedError
