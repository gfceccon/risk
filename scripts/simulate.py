from risk import RiskGame
from risk.map import world_map
from risk.players import PlayerRandom

def simulate(games: int = 1 ) -> None:
    player1 = PlayerRandom("Alice", 1)
    player2 = PlayerRandom("Bob", 2)
    game = RiskGame([player1, player2], world_map)
    print("Game over!")