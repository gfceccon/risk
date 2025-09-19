from typing import List, Sequence, Tuple
from risk.game.map.map import Map
from risk.metrics.metrics import Metrics
from risk.game.base.game_base import PlayerAbstract
from risk.game.state import State


class Game:
    state: State
    metrics: Metrics
    num_troops_start: int

    def __init__(self, players: List[PlayerAbstract], game_map: Map):
        self.state = State(players, game_map)
        self.metrics = Metrics()
        self.reset()

    def get_troops(self) -> int:
        num_players = len(self.state.players)
        if num_players == 3:
            return 35
        elif num_players == 4:
            return 30
        elif num_players == 5:
            return 25
        elif num_players == 6:
            return 20
        else:
            raise ValueError("Number of players must be between 3 and 6.")

    def reset(self):
        self.state.reset(self.get_troops())
        for player in self.state.players:
            player.reset(self.state)

    def step(self) -> State:
        player = self.state.player_turn
        action = player.step(self.state)
        self.state.apply_action(action)
        self.state = self.state.next_state()

        return self.state

    def add_metrics(self, name: str, value: float | str | object) -> None:
        self.metrics.add(name, value)

    def play(self) -> None:
        while not self.state.is_terminal():
            self.step()
