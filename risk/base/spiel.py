from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
import numpy as np
import pyspiel


class PyspielGame(pyspiel.Game):
    def __init__(self, game_type: pyspiel.GameType, game_info: pyspiel.GameInfo, params=None):
        super().__init__(game_type, game_info, params or {})

    @abstractmethod
    def new_initial_state(self) -> pyspiel.State:
        pass

    @abstractmethod
    def make_py_observer(self, iig_obs_type=None, params=None) -> 'PyspielObserver':
        pass


class PyspielState(pyspiel.State):
    def __init__(self, game: PyspielGame):
        super().__init__(game)
        self.game = game

    @abstractmethod
    def _legal_actions(self, player: int) -> List[int]:
        pass

    @abstractmethod
    def _apply_action(self, action: int) -> None:
        pass

    @abstractmethod
    def _action_to_string(self, player: int, action: int) -> str:
        pass

    @abstractmethod
    def chance_outcomes(self) -> List[Tuple[int, float]]:
        pass

    @abstractmethod
    def current_player(self) -> int:
        pass

    @abstractmethod
    def is_terminal(self) -> bool:
        pass

    @abstractmethod
    def returns(self) -> List[float]:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class PyspielObserver(ABC):
    def __init__(self, iig_obs_type, params=None):
        if iig_obs_type.private_info == pyspiel.PrivateInfoType.SINGLE_PLAYER:
            self.dict = self._iig_private_single_player()
        elif iig_obs_type.public_info == pyspiel.PublicInfoType.PUBLIC:
            if iig_obs_type.perfect_recall:
                self.dict = self._iig_public_perfect_recall()
            else:
                self.dict = self._iig_public()
        self.tensor = np.zeros(self._tensor_size(), dtype=np.float32)

    @abstractmethod
    def _iig_private_single_player(self) -> Dict:
        pass

    @abstractmethod
    def _iig_public(self) -> Dict:
        pass

    @abstractmethod
    def _iig_public_perfect_recall(self) -> Dict:
        pass

    @abstractmethod
    def _tensor_size(self) -> int:
        pass

    @abstractmethod
    def set_from(self, state: PyspielState, player: int) -> None:
        pass

    @abstractmethod
    def string_from(self, state: PyspielState, player: int) -> str:
        pass
