# TODO

Implementations marked with an asterisk (*) are optional and can be deferred to later stages.
Testing and documentation should be integrated throughout the development process, after each major feature or component is implemented.

## Game Features
Features and components of the game.

- [ ] Game State
    - [x] Territory
    - [ ] Army
    - [x] Graph Representation
    - [ ] Cards *
        - [ ] Army Trading
    - [ ] Objectives
        - [ ] World Domination
        - [ ] Player Kill *
        - [ ] Specific (e.g., "Conquer North America") *
        - [ ] Generic (e.g., "Conquer 24 territories") *

## Game Mechanics
Gameplay mechanics and rules.

- [ ] Setup
    - [ ] Dice Rolling
    - [ ] Starting Player Selection
    - [ ] Initial Army Placement
    - [ ] Objective Cards *
- [ ] Turn Order
    - [ ] Reinforcement
    - [ ] Attacking
    - [ ] Fortifying
- [ ] Combat
    - [ ] Dice Rolling
    - [ ] Battle Resolution
    - [ ] Decision Making (AI/Player)
- [ ] Card Trading *
    - [ ] Army Placement
- [ ] Objective Completion
    - [ ] Victory Conditions
    - [ ] Objective Cards *
- [ ] Game End Conditions

## Docker
Docker setup for containerized deployment.

- [ ] Dockerfile
- [ ] docker-compose.yml

## Reinforcement Learning
Components for implementing reinforcement learning agents.

- [ ] State Representation
    - [ ] Game State Encoding
- [ ] Action Space
    - [ ] Valid Actions
- [ ] Reward Structure
    - [ ] Win/Loss Rewards
- [ ] Training Loop
    - [ ] Self-Play
- [ ] Agent
- [ ] Evaluation Metrics

## User Interface
Scripts for simulation and visualization.

- [ ] Simulation Mode
    - [ ] Automated Gameplay
    - [ ] Visualization
    - [ ] Statistics Tracking
    - [ ] CLI Options
        - [ ] Number of Agents
        - [ ] Agent Types (e.g., Random, RL-based)
        - [ ] Map Selection
        - [ ] Number of Games
        - [ ] RL Training Parameters *
- [ ] Command Line Interface (CLI) *
    - [ ] Game Setup *
    - [ ] Player Interaction *
    - [ ] Display Game State *

## Metrics
Metrics for evaluating game performance and agent effectiveness.

- [ ] Win Rate
- [ ] Average Game Length
- [ ] Average Explored States
- [ ] Average Rewards