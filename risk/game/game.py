from typing import List, Sequence, Tuple
from risk.game.base.map_base import MapBase
from risk.game.base.config import Config, default_config
from risk.metrics.metrics import Metrics
from risk.game.base.game_base import PlayerBase
from risk.game.state import State


class Game:
    state: State
    metrics: Metrics
    num_troops: int

    def __init__(self, players: List[PlayerBase], game_map: MapBase, config: Config = default_config):
        self.config = config
        self.state = State(players, game_map)
        self.metrics = Metrics()
        self.reset()

    def get_troops(self) -> int:
        return self.config.INITIAL_TROOPS.get(len(self.state.players), 0)

    def reset(self):
        self.num_troops = self.get_troops()
        self.state.reset()
        for player in self.state.players:
            player.reset()

    def add_metrics(self, name: str, value: float | str | object) -> None:
        self.metrics.add(name, value)

    def play(self) -> None:
        while not self.state.is_terminal():
            player = self.state.player_turn
            legal_actions = self.state.legal_actions()
            action = player.pick(legal_actions)
            for agent in self.state.players:
                agent.step(player, action)
            self.state.apply_action(action)
            self.state = self.state.next_state()
