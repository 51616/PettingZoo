
### Prospector

This environment is part of the [gamma environments](../gamma.md). Please read that page first for general information.

| Actions    | Agents  | Manual Control | Action Shape    | Action Values       | Observation Shape              | Observation Values        | Num States |
|------------|---------|----------------|-----------------|---------------------|--------------------------------|---------------------------|------------|
| Continuous | 7 (+/-) | Yes            | (3,)            | [-1, 1]             | (150, 150, 3) or (154, 154, 3) | (0, 255)                  | ?          |

`from pettingzoo.gamma import prospector_v0`

`agents= ["prospector_0, "prospector_1", "prospector_2", "prospector_3", "banker_0", "banker_1", "banker_2"]`

![](gamma_prospector.gif)

*AEC diagram*

This game is inspired by gold panning in the American "wild west" movies. There's a blue river at 
the bottom of the screen, which contains gold. 4 "prospector" agents can move and touch the river 
and pan from it, and get a gold nugget (visibly held by them). They take a 3 element vector of 
continuous values (the first for forward/backward, the second for left/right movement, the third 
for clockwise/counter-clockwise rotation). They can only hold 1 nugget at a time.

There are a handful of bank chests at the top of the screen. The prospector agents can hand their 
held gold nugget to the 3 "banker" agents, to get a reward. The banker agents can't rotate, 
and the prospector agents must give the nuggets (which are held in the same
position relative to the prospector's position and rotation) to the 
front of the bankers (within a plus or minus 45 degree tolerance). 
The bankers then get the gold, and can deposit it into the chests to recieve a reward. 
They take a 3 element vector of continuous values 
(the first for forward/backward, the second for left/right movement, the
third value is not used since bankers can't rotate). They can only hold 1 
nugget at a time. 

Rewards are issued for a prospector retrieving a nugget, a prospector handing
a nugget off to a banker, a banker receiving a nugget from a prospector, 
and a banker depositing the gold into a bank. There is
an individual reward, a group reward (for agents of the same type), and
an other-group reward (for agents of the other type).

Manual Control:

`"prospector_0"` is the first sprite you control. Use the left and
right arrow keys to switch between the agents.

Move prospectors using the 'WASD' keys for forward/left/backward/right movement.
Rotate using 'QE' for counter-clockwise/clockwise rotation.

Move the bankers using the 'WASD' keys for forward/left/backward/right movement.

The game lasts for 900 frames by default.

**Arguments:**

```
prospector_v0.env(ind_reward=0.8, group_reward=0.1, other_group_reward=0.1, 
prospec_find_gold_reward=1, prospec_handoff_gold_reward=1, banker_receive_gold_reward=1,
banker_deposit_gold_reward=1, max_frames=900, seed=None)
```

**About arguments:**

`ind_reward`: The reward multiplier for a single agent completing an objective.

`group_reward`: The reward multiplier that agents of the same type
as the scoring agent will earn.

`other_group_reward`: The reward multiplier that agents of the other type
as the scoring agent will earn. If the scoring agent is a prospector,
then this is the reward that the bankers get, and vice versa.

Constraint: `ind_reward + group_reward + other_group_reward == 1.0`

`prospec_find_gold_reward`: The reward for a prospector
retrieving gold from the water at the bottom of the screen.

`prospec_handoff_gold_reward`: The reward for a prospector
handing off gold to a banker.

`banker_receive_gold_reward`: The reward for a banker receiving
gold from a prospector.

`banker_deposit_gold_reward`: The reward for a banker depositing
gold into a bank.

`max_frames`: The number of frames the game should run for.

`seed`: Non-negative integer or None, sets the seed for the random
number generator. This generator is used to determine
agent starting locations.

Leaderboard:

| Average Total Reward | Method | Institution | Paper | Code |
|----------------------|--------|-------------|-------|------|
| x                    | x      | x           | x     | x    |
