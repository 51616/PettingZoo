## Butterfly Environments

| Environment             | Actions    | Agents  | Manual Control | Action Shape | Action Values | Observation Shape | Observation Values | Num States |
|:------------------------|:-----------|:-------:|:--------------:|:------------:|:-------------:|:-----------------:|:------------------:|----------:|
| [Cooperative Pong](cooperative_pong)        | Discrete   | 2       | Yes            | ?            | ?             | ?                 | ?                  | ?          |
| [Knights Archers Zombies](knights_archers_zombies) | Discrete   | 4 (+/-) | Yes            | (1,)         | [0, 5]        | (512, 512, 3)     | (0, 255)           | ?          |
| [Pistonball](pistonball)              | Either     | 20      | Yes            | (1,)         | [0, 2]        | (200, 120, 3)     | (0, 255)           | ?          |
| [Prison](prison)                  | Either     | 8 (+/-) | Yes            | (1,)         | [0, 2]        | (100, 300, 3)     | (0, 255)           | ?          |
| [Prospector](prospector)              | Continuous | 7 (+/-) | Yes            | ?            | ?             | ?                 | ?                  | ?          |

`pip install pettingzoo[butterfly]`

All butterfly environments were created by us, using PyGame, with visual Atari spaces. In Prison, all agents are completely independent (i.e. no coordination is possible, each agent is in it's own cell. It is intended as a debugging tool.

All other environments require a high degree of coordination and learning emergent behaviors to achieve an optimal policy. As such, these environments are currently very challenging to learn.

All environments are highly configurable with environment arguments.
