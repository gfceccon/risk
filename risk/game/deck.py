from dataclasses import dataclass
from risk.map.territory import Territory


@dataclass
class Card:
    territory: Territory
    type: int


class Deck:
    cards: list[Card]
    discarded: list[Card]
    trade_count: int = 0
    trade_values: list[int] = [4, 6, 8, 10, 12, 15]

    def __init__(self, territories: list[Territory]):
        self.cards = [Card(territory, i % 3)
                      for i, territory in enumerate(territories)]
        self.discarded = []
        self.shuffle()

    def shuffle(self) -> None:
        import random
        cards = self.cards + self.discarded
        random.shuffle(cards)
        self.cards = cards
        self.discarded = []

    def draw(self) -> Card:
        if not self.cards:
            self.shuffle()
        return self.cards.pop()

    def trade(self, cards: list[Card]) -> int:
        if len(cards) != 3:
            raise ValueError("Must trade exactly 3 cards")
        types = [card.type for card in cards]
        if len(set(types)) == 1 or len(set(types)) == 3:
            for card in cards:
                self.discarded.append(card)
            return 1
        else:
            raise ValueError(
                "Invalid trade: must be all same type or all different types")
