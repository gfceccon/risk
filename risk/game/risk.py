from risk.base.config import _GAME_TYPE, _GAME_INFO, GetGameInfo
from risk.base.spiel import PyspielGame, PyspielState, PyspielObserver
from risk.base.player import PlayerBase
from risk.game.deck import Deck
from risk.map import Map
import pyspiel


class RiskGame(PyspielGame):
    def __init__(self, params):
        super().__init__(_GAME_TYPE, GetGameInfo(Map.get_map_specs(params.get('map', 'world'))), params or {})
        self.game_map = Map.get_map_by_name(params.get('map', 'world'))

    def new_initial_state(self) -> PyspielState:
        return RiskState(self, self.game_map)

    def make_py_observer(self, iig_obs_type=None, params=None) -> 'PyspielObserver':
        return RiskObserver(iig_obs_type, params)


class RiskState(PyspielState):
    game_map: Map
    deck: Deck
    players: list[PlayerBase]

    def __init__(self, game: PyspielGame, game_map: Map):
        super().__init__(game)
        self.game_map = game_map
        self.players = []
        self.deck = Deck(game_map)

    def initialize(self, players: list[type[PlayerBase]]) -> None:
        for i, player_cls in enumerate(players):
            player = player_cls(id=i, name=f"Player {player_cls.__name__} #{i+1}")
            self.players.append(player)
        self.deck.shuffle()
        self.game_map.reset()

        if len(players) == 2:
            from risk.players import PlayerNoOp
            self.players.append(PlayerNoOp(
                id=2, name=f"Player {PlayerNoOp.__name__} #3"))
            cards_size = len(self.deck.cards) // 3
            for player in self.players:
                for _ in range(cards_size):
                    card = self.deck.draw()
                    card.territory.owner = player.id

        return None

    def _legal_actions(self, player: int) -> list[int]:
        # Return a list of legal actions for the given player
        return []

    def _apply_action(self, action: int) -> None:
        # Apply the given action to the game state
        return None

    def _action_to_string(self, player: int, action: int) -> str:
        # Convert an action to a human-readable string
        return ""

    def chance_outcomes(self) -> list[tuple[int, float]]:
        # Return a list of possible chance outcomes and their probabilities
        return []

    def current_player(self) -> int:
        # Return the index of the current player
        return 0

    def is_terminal(self) -> bool:
        # Return True if the game is over, False otherwise
        return False

    def returns(self) -> list[float]:
        # Return the returns for each player at the end of the game
        return []

    def __str__(self) -> str:
        # Return a string representation of the current game state
        return ""


class RiskObserver(PyspielObserver):
    def __init__(self, iig_obs_type, params=None):
        super().__init__(iig_obs_type, params)
        # Initialize observer state here

    def _iig_private_single_player(self) -> dict:
        # Return private information for a single player
        return {}

    def _iig_public(self) -> dict:
        # Return public information about the game state
        return {}

    def _iig_public_perfect_recall(self) -> dict:
        # Return public information with perfect recall
        return {}

    def _tensor_size(self) -> int:
        # Return the size of the observation tensor
        return 0

    def set_from(self, state: PyspielState, player: int) -> None:
        # Update the observer's state based on the given game state and player
        return

    def string_from(self, state: PyspielState, player: int) -> str:
        # Return a string representation of the observation for the given player
        return ""


pyspiel.register_game(_GAME_TYPE, RiskGame)
