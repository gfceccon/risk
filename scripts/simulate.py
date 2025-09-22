from risk.players import PlayerRandom
import pyspiel


def simulate(games: int = 1) -> None:
    game = pyspiel.load_game(
        "risk_python", {
            "players": 2,
            "map": "three_territories"
        })
    state = game.new_initial_state()
    state.initialize([PlayerRandom, PlayerRandom])
    print("Game over!")
