# Partial reward function ideas
- Reward = norm(norm(territories) * norm(troops))
    - e.g 3 total territories, 17 total troops
    - player 1 has 2 territories and 5 troops
    - player 2 has 1 territory and 12 troops
    - player 1 reward = (2/3) * (5/17) = 0.196
    - player 2 reward = (1/3) * (12/17) = 0.235
    - norm player 1 = 0.196 / (0.196 + 0.235) = 0.455
    - norm player 2 = 0.235 / (0.196 + 0.235) = 0.545

# Risk function ideas
- Over time attacks
    - More attacks = more risk
    - More successful attacks = less risk
    - Failed attacks = more risk

# Capture function ideas
- More enemies borders, less capture incentive
- More allies borders, more capture incentive
- More % of continent owned, more capture incentive
- Objective cards, more capture incentive

# Objective decision ideas
- Kill weaker players can lead to better positions
- Find best route to target territory
- Find territories that are crucial to defend (e.g choke points)
