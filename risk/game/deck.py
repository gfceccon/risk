from dataclasses import dataclass
from risk.map import Map, Territory


@dataclass
class Card:
    territory: Territory
    type_name: str
    type: int


class Deck:
    cards: list[Card]
    discarded: list[Card]
    card_types: list[str]
    trade_bonus: list[int]
    trade_count: int

    def __init__(self, map: Map):
        self.cards = []
        self.discarded = []
        self.trade_count = 0
        self.card_types = map.deck_card_types
        self.trade_bonus = map.deck_army_bonus
        territories = sorted([t for continent in map.continents
                              for t in continent.territories],
                             key=lambda x: x.id)
        for i, territory in enumerate(territories):
            type_idx = i % len(self.card_types)
            self.cards.append(
                Card(territory=territory,
                     type_name=self.card_types[type_idx],
                     type=type_idx)
            )
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
        types = [card.type for card in cards]
        types_set = set(types)
        if (len(types_set) == 1 or
                len(types_set) == len(self.card_types)):
            for card in cards:
                self.discarded.append(card)
            return self.trade_bonus[min(self.trade_count, len(self.trade_bonus) - 1)]
        return 0
