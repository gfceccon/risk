from scripts.simulate import simulate
import argparse

parser = argparse.ArgumentParser(description="Simulate Risk games.", add_help=True)
parser.add_argument('--games', '-games', dest="games", type=int, default=1, help='Number of games to simulate', required=True)

if __name__ == "__main__":
    args = parser.parse_args()
    simulate(args.games)