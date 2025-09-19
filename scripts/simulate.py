from risk import Game, PlayerRL, PlayerRandom, World

def simulate():
    world = World()
    player1 = PlayerRandom(1, "Alice")
    player2 = PlayerRandom(2, "Bob")
    game = Game([player1, player2], world)
    game.play()
    print("Game over!")