import numpy as np
from environment import Environment
from agent import QLearningAgent,SarsaAgent
from maze import draw_maze

# 定义迷宫：0表示通道，1表示障碍
maze = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]

episodes = 100

env = Environment(maze)
type = input("Enter 1 for Q-Learning or 2 for SARSA:")
if type=="1":
    agent = QLearningAgent(actions=[0, 1, 2, 3])
    for episode in range(episodes):
        state = env.reset()
        done = False
        path = [state]

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
            path.append(state)

        if episode % 10 == 0:
            print(f"Episode {episode}: Path taken: {path}")
elif type=="2":
    agent = SarsaAgent(actions=[0, 1, 2, 3])
    for episode in range(episodes):
        state = env.reset()
        done = False
        path = [state]

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            next_action = agent.choose_action(next_state)
            agent.learn(state, action, reward, next_state, next_action)
            state = next_state
            path.append(state)

        if episode % 10 == 0:
            print(f"Episode {episode}: Path taken: {path}")

#when the Q table is fully updated, we can use it to find the optimal path by following the action with the highest Q value at each state
final_state = env.reset()
final_path = [final_state]
done = False
while not done:
    action = agent.choose_action_greedy(final_state)
    final_state, _, done = env.step(action)
    final_path.append(final_state)
print("Final path: ", final_path)
draw_maze(maze, path)

