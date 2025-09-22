from risk.base.player import PlayerBase


class PlayerNoOp(PlayerBase):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)

    def reset(self) -> None:
        return None

    def pick(self, legal_actions: list[int]) -> int:
        return 0

    def step(self, player: 'PlayerBase', action: int) -> None:
        return None
