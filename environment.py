import numpy as np

class Environment:
    def __init__(self, maze):
        self.maze = maze
        self.start_state = (0, 0)
        self.end_state = (len(maze) - 1, len(maze[0]) - 1)
        self.reset()

    def reset(self):
        self.state = self.start_state
        return self.state

    def step(self, action):
        x, y = self.state
        if action == 0:    # 上
            next_state = (max(x - 1, 0), y)
        elif action == 1:  # 下
            next_state = (min(x + 1, len(self.maze) - 1), y)
        elif action == 2:  # 左
            next_state = (x, max(y - 1, 0))
        elif action == 3:  # 右
            next_state = (x, min(y + 1, len(self.maze[0]) - 1))

        if self.maze[next_state[0]][next_state[1]] == 1:  # 1表示障碍
            next_state = self.state  # 如果是障碍，则不移动

        reward = 10 if next_state == self.end_state else -1
        self.state = next_state
        return next_state, reward, next_state == self.end_state

    def get_possible_actions(self):
        return [0, 1, 2, 3]  # 上下左右
