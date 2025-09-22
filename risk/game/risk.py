from risk.base.config import _GAME_TYPE, _GAME_INFO
from risk.base.spiel import PyspielGame, PyspielState, PyspielObserver
from risk.game.deck import Deck
from risk.map import Map, world_map
import pyspiel


class RiskGame(PyspielGame):
    def __init__(self, params=None, map: Map = world_map):
        self.game_parameters = self.get_parameters()
        self.map = map
        assert "num_territories" in self.game_parameters, "num_territories parameter is required"
        assert "num_borders" in self.game_parameters, "num_borders parameter is required"

        super().__init__(_GAME_TYPE, _GAME_INFO(
            self.game_parameters["num_territories"],
            self.game_parameters["num_borders"]),
            params or {})

    def new_initial_state(self) -> PyspielState:
        return RiskState(self, self.map)

    def make_py_observer(self, iig_obs_type=None, params=None) -> 'PyspielObserver':
        return RiskObserver(iig_obs_type, params)


class RiskState(PyspielState):
    deck: Deck

    def __init__(self, game: PyspielGame, map: Map):
        super().__init__(game)
        self.map = map
        # Initialize the state of the game here (e.g., territories, players, etc.)

    def initialize(self) -> None:
        # Set up the initial state of the game
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
