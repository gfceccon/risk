# Risk AI Agent

This project is an AI agent designed to play the classic board game Risk. The agent analyzes the game state, makes strategic decisions and competes against human or other AI players. This is a reinforcement learning project using TensorFlow. The implementation is a smaller scale version of Risk, played on a simplified map with fewer territories and players.

### Prerequisites

- Python 3.12
- Poetry (for dependency management)

### Installation

```bash
git clone https://github.com/gfceccon/risk.git
cd risk
poetry install
```

### Usage

To run a simple game simulation:

```bash
poetry run python scripts/game.py
```

To see the arguments you can pass to the script:

```bash
poetry run python scripts/game.py --help
```

## License

This project is licensed under the Creative Commons CC0-1.0. See the LICENSE file for details.