## Introduction
This repo uses a simple maze problem to show how Q-learning and Sarsa works. Aims to help you understand the basic idea of reinforcement learning.

The maze is a 4*4 maze, and the agent is in the start point (0,0) and the goal is in the end point (3,3). And you can change the maze as you want, such as the size of the maze, the start point, the goal point, the wall point and so on.

The agent can move in four directions: up, down, left, right. The agent can get a reward of -1 for each step, and get a reward of 10 for reaching the goal. The agent can't move out of the maze and it can't move to the wall.

## Introduction to Q-learning and Sarsa
#### Q-value Function

The Q-value function is defined as: Q(s, a) = R(s, a) + γ max_a' Q(s', a')

where:
- **Q(s, a)**: The expected return of taking action **a** in state **s**.
- **R(s, a)**: The immediate reward for taking action **a** in state **s**.
- **γ**: Discount factor, **0 ≤ γ < 1**.
- **s'**: The next state.
- **a'**: Possible actions.
### Q-learning Principle

Q-learning is an offline reinforcement learning algorithm used to estimate the value of taking a specific action in a specific state. It achieves this by learning a **Q-value** function.

#### Update Rule

When we get an (S,A,R,S') tuple, we can update the Q-value using the following rule:

Q(s, a) ← Q(s, a) + α [R(s, a) + γ max_a' Q(s', a') - Q(s, a)]

where:
- **α**: Learning rate, which determines the weight of new information in the update.
- **a'**: The action that maximizes the Q-value in the next state **s'**.

### Sarsa Principle

Sarsa is an online reinforcement learning algorithm that uses the actual action taken under the current policy to update the Q-value, rather than the optimal action.

#### Update Rule

When we get an (S,A,R,S',A') tuple, we can update the Q-value using the following rule:

Q(s, a) ← Q(s, a) + α [R(s, a) + γ Q(s', a') - Q(s, a)]

where:
-  **a'** is the action chosen in state **s'** according to the current policy.

## Differences between Q-learning and Sarsa

The main difference between Q-learning and Sarsa is that Q-learning is an off-policy algorithm, while Sarsa is an on-policy algorithm.
Which means that Q-learning only needs (S,A,R,S') to update the Q-value {actually it also uses (S,A,R,S',A') pair, but A' is not sampled. We use greedy strategy to choose the action A' based on our "experience".}, while Sarsa needs real (S,A,R,S',A') pair to update the Q-value. And this difference can be found in main.py.