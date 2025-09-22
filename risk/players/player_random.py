from risk.base.player import PlayerBase


class PlayerRandom(PlayerBase):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)

    def reset(self) -> None:
        pass

    def pick(self, legal_actions: list[int]) -> int:
        import random
        return random.choice(legal_actions)

    def step(self, player: PlayerBase, action: int) -> None:
        pass
