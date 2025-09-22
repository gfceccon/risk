import os
from risk.map import Continent, Territory


class Map:
    continents: list[Continent]
    deck_army_bonus: list[int]
    deck_card_types: list[str]
    num_territories: int
    num_borders: int

    def __init__(self):
        self.continents = []
        self.deck_army_bonus = []
        self.deck_card_types = []
        self.num_territories = 0
        self.num_borders = 0

    def reset(self) -> None:
        for continent in self.continents:
            continent.reset()

    def add_borders(self, borders: list[tuple[Territory, Territory]]):
        for t1, t2 in borders:
            if t2 not in t1.borders:
                t1.add_border(t2)

    @classmethod
    def from_json(cls, file_name: str) -> 'Map':
        game_map = cls()
        file_path = os.path.join(os.path.dirname(__file__), 'maps', file_name)
        import json

        with open(file_path, 'r') as f:
            data = json.load(f)

        for continent_id, continent_data in enumerate(data["continents"]):
            continent = Continent(
                id=continent_id,
                name=continent_data["name"],
                territories=[
                    Territory(id=territory["id"],
                              name=territory["name"],
                              continent_id=continent_id)
                    for territory in continent_data["territories"]
                ],
                bonus=continent_data["bonus"]
            )
            game_map.continents.append(continent)
        borders = []

        for continent_data in data["continents"]:
            continent = next((c for c in game_map.continents
                              if c.name == continent_data["name"]), None)
            if continent is None:
                continue

            game_map.num_territories += len(continent.territories)

            for territory_data in continent_data["territories"]:
                territory = next(
                    t for t in continent.territories
                    if t.name == territory_data["name"])
                for neighbor_name in territory_data["borders"]:
                    neighbor = continent.get_territory_by_name(neighbor_name)
                    if neighbor:
                        game_map.num_borders += 1
                        borders.append((territory, neighbor))

        if "deck" in data:
            deck_data = data["deck"]
            if "army_bonus" in deck_data:
                game_map.deck_army_bonus = deck_data["army_bonus"]
            if "types" in deck_data:
                game_map.deck_card_types = deck_data["types"]

        game_map.add_borders(borders)
        return game_map

    def __str__(self) -> str:
        result = ""
        for continent in self.continents:
            result += f"{continent}\n"
        return result
    
    @staticmethod
    def get_map_specs(map_name: str) -> tuple[int, int]:
        match map_name:
            case "world":
                return Map.WORLD.num_territories, Map.WORLD.num_borders
            case "three_territory":
                return Map.THREE_TERRITORY.num_territories, Map.THREE_TERRITORY.num_borders
            case _:
                return Map.WORLD.num_territories, Map.WORLD.num_borders
            
    @staticmethod
    def get_map_by_name(map_name: str) -> 'Map':
        match map_name:
            case "world":
                return Map.WORLD
            case "three_territory":
                return Map.THREE_TERRITORY
            case _:
                return Map.WORLD

    WORLD: 'Map'
    THREE_TERRITORY: 'Map'