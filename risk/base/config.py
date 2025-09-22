import pyspiel

_MAX_NUM_PLAYERS = 6
_MIN_NUM_PLAYERS = 2
_NUM_TERRITORIES_WORLD = 42  # 42 territories on the board (world map)
_NUM_BORDERS_WORLD = 84  # 84 borders on the board (world map)

# Attackers can roll 1, 2, or 3 dice
# Defenders can roll 1 or 2 dice
# So max dice rolls = 3 * 2 = 6

_MAX_OUTCOMES = 6  # 6 outcomes for dice rolls
_MAX_GAME_LENGTH = 1_000_000  # Infinite turns, theoretically

_NUM_ACTIONS_PER_TERRITORY = 3  # 0: no action, 1: attack, 2: fortify
_NUM_ACTIONS_CARD = 3  # 0: no card action, 1: receive card, 2: trade in cards
_DISTINCT_ACTIONS_BASE = (
    _MAX_NUM_PLAYERS * _NUM_ACTIONS_PER_TERRITORY *
    _NUM_ACTIONS_CARD * _MAX_OUTCOMES *
    _NUM_TERRITORIES_WORLD * _NUM_BORDERS_WORLD
)


INITIAL_TROOPS: dict[int, int] = {
    3: 35,
    4: 30,
    5: 25,
    6: 20,
}

CONTINENT_BONUSES: dict[str, int] = {
    "north_america": 1,
    "south_america": 1,
    "europe": 1,
    "africa": 1,
    "asia": 1,
    "australia": 1,
}


_GAME_TYPE = pyspiel.GameType(
    short_name="risk_python",
    long_name="Python Risk",
    dynamics=pyspiel.GameType.Dynamics.SEQUENTIAL,
    chance_mode=pyspiel.GameType.ChanceMode.EXPLICIT_STOCHASTIC,
    information=pyspiel.GameType.Information.IMPERFECT_INFORMATION,
    utility=pyspiel.GameType.Utility.ZERO_SUM,
    reward_model=pyspiel.GameType.RewardModel.TERMINAL,
    max_num_players=_MAX_NUM_PLAYERS,
    min_num_players=_MIN_NUM_PLAYERS,
    provides_information_state_string=False,
    provides_information_state_tensor=False,
    provides_observation_string=False,
    provides_observation_tensor=False,
    parameter_specification={
        "players": _MIN_NUM_PLAYERS,
        "map": "world",
    },
)


_GAME_INFO = pyspiel.GameInfo(
    num_distinct_actions=_DISTINCT_ACTIONS_BASE,
    max_chance_outcomes=_MAX_OUTCOMES,
    num_players=_MIN_NUM_PLAYERS,
    min_utility=-1,
    max_utility=1,
    utility_sum=0.0,
    max_game_length=_MAX_GAME_LENGTH,
)


def GetGameInfo(map_specs: tuple[int, int] = (_NUM_TERRITORIES_WORLD, _NUM_BORDERS_WORLD)) -> pyspiel.GameInfo:
    return pyspiel.GameInfo(
        num_distinct_actions=(
            _MAX_NUM_PLAYERS * _NUM_ACTIONS_PER_TERRITORY *
            _NUM_ACTIONS_CARD * _MAX_OUTCOMES *
            map_specs[0] * map_specs[1]
        ),
        max_chance_outcomes=_MAX_OUTCOMES,
        num_players=_MIN_NUM_PLAYERS,
        min_utility=-1,
        max_utility=1,
        utility_sum=0.0,
        max_game_length=_MAX_GAME_LENGTH,
    )
