## Atari Environments

| Environment | Actions | Agents  | Manual Control | Action Shape | Action Values | Observation Shape | Observation Values |
|--------------|---------|---------|----------------|--------------|---------------|-------------------|--------------------|
| [Boxing](atari/boxing)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Combat: Tank](atari/combat_tank)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Combat: Plane](atari/combat_plane)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Double Dunk](atari/double_dunk)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Entombed: Competitive](atari/entombed_competitive)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Entombed: Cooperative](atari/entombed_cooperative)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Flag Capture](atari/flag_capture)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Joust](atari/joust)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Ice Hockey](atari/ice_hockey)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Maze Craze](atari/maze_craze)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Mario Bros](atari/mario_bros)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Othello](atari/othello)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Pong: Classic](atari/pong_classic)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Pong: Basketball](atari/pong_basketball)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Pong: Foozpong](atari/pong_foozpong)   | Discrete  | 4 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Pong: Quadrapong](atari/pong_quadrapong)   | Discrete  | 4 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Pong: Team Volleyball](atari/pong_volleyball)   | Discrete  | 4 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Space Invaders](atari/space_invaders)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Space War](atari/space_war)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Surround: Original](atari/surround)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Tennis](atari/tennis)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Video Checkers](atari/video_checkers)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Wizard of Wor](atari/wizard_of_wor)   | Discrete  | 2 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |
| [Warlords](atari/warlords)   | Discrete  | 4 | No      | (1,)    | [0,17]         | (210, 160, 3)         | (0,255)            |


The Atari environments are based off the [Arcade Learning Environment](https://github.com/mgbellemare/Arcade-Learning-Environment). This environment was instrumental in the development of modern reinforcement learning, and so we hope that our [multi-agent version](https://github.com/PettingZoo-Team/Multi-Agent-ALE) of it will be useful in the development of multi-agent reinforcement learning.

### Games overview

Most games are two player, with the exception of Warlords and a couple of Pong variations which are four player.

There are three types of games:

### Environment details

The ALE environment has been studied extensively and examined for various flaws and how to fix them.  

* Determinism: The Atari console is deterministic, and so agents can theoretically memorize precise sequences of actions that will maximize the end score. This is not ideal, so we enable *sticky actions*, controlled by the `repeat_action_probability` environment parameter, by default. This is the recommended approach of  *"Machado et al. (2018), "Revisiting the Arcade Learning Environment: Evaluation Protocols and Open Problems for General Agents"*

### Preprocessing

We encourage the use of the [supersuit](https://github.com/PettingZoo-Team/SuperSuit) library for preprocessing. This library can be installed with `pip install supersuit`.

Here is some example usage for the Atari preprocessing that is default in gym.

```
from supersuit import down_scale, frame_skip
from pettingzoo.atari import space_invaders_v0
env = space_invaders_v0.env()
env = frame_skip(env, (2,5))
env = down_scale(env, ???)
```

### Common Parameters

All the Atari environments have the following environment parameters:

```
<atar_game>.env(seed=None, obs_type='rgb_image', frameskip=3, repeat_action_probability=0.25, full_action_space=True)
```

```
seed: Set to specific value for deterministic, reproducible behavior.

obs_type: default value of 'rgb_image' leads to (210, 160, 3) image pixel observations like you see as a human, 'grayscale_image' leads to a black and white (210, 160, 1) image, 'ram' leads to an observation of the 1024 bits that comprise the RAM of the atari console.

repeat_action_probability: probability you repeat an action from the previous frame (not step, frame), even after you have chosen a new action. Simulates the joystick getting stuck and not responding 100% quickly to moves.

full_action_space: The effective action space of the atari games is often smaller than the full space of 18 moves. Setting this to False shrinks the action space to this smaller space.
```

### Citation

If you use the Atari environments in your research please cite the following paper:

```
@Article{bellemare13arcade,
  author = { {Bellemare}, M.~G. and {Naddaf}, Y. and {Veness}, J. and {Bowling}, M.},
  title = {The Arcade Learning Environment: An Evaluation Platform for General Agents},
  journal = {Journal of Artificial Intelligence Research},
  year = "2013",
  month = "jun",
  volume = "47",
  pages = "253--279",
}
```
