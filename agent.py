import numpy as np
from MLP import MLP
class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)  # 探索
        return np.argmax(self.q_table.get(state, np.zeros(len(self.actions))))  # 利用

    def learn(self, state, action, reward, next_state):
        q_value = self.q_table.get(state, np.zeros(len(self.actions)))
        next_q_value = self.q_table.get(next_state, np.zeros(len(self.actions)))
        q_value[action] += self.alpha * (reward + self.gamma * np.max(next_q_value) - q_value[action])
        self.q_table[state] = q_value

    def choose_action_greedy(self, state):
        return np.argmax(self.q_table.get(state, np.zeros(len(self.actions))))

class SarsaAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)  # 探索
        return np.argmax(self.q_table.get(state, np.zeros(len(self.actions))))  # 利用

    def learn(self, state, action, reward, next_state,next_action):
        q_value = self.q_table.get(state, np.zeros(len(self.actions)))
        next_q_value = self.q_table.get(next_state, np.zeros(len(self.actions)))
        q_value[action] += self.alpha * (reward + self.gamma * next_q_value[next_action] - q_value[action])
        self.q_table[state] = q_value

    def choose_action_greedy(self,state):
        return np.argmax(self.q_table.get(state, np.zeros(len(self.actions))))