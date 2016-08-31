import random

class QLearner():
    """A QLearner Implementation"""

    def __init__(self, actions, Q_init=2, gamma=0.8):
        self.ACTIONS = actions
        self.QTable = {}
        self.Q_init = Q_init # initial `Q_hat` value arbitrarily
        self.gamma = gamma # discounting rate
        self.epsilon = 0.5 # exploration rate
        self.alpha = 0.5 # learning rate


    def next_action(self, state):
        if self.QTable.has_key(state):  # is this a state familiar (we've seen it before)
            if random.random() < self.epsilon:
                # get the action of max reward
                max_reward_actions = [ action for action, Q_hat in self.QTable[state].items() \
                                        if Q_hat == max(self.QTable[state].values()) ]
                # choose randomly if more than 1 argmax action
                return random.choice(max_reward_actions)
            else:
                return random.choice(self.ACTIONS)
        else:
            # log the state into our QTable
            self.QTable.update({
                state: {None: self.Q_init, 'forward': self.Q_init, 'left': self.Q_init, 'right': self.Q_init}
            })
            # then choose a random action
            # TODO: update this to follow driving rules
            return random.choice(self.ACTIONS)


    def update(self, state, previous, steps_count):
        Qtable = self.QTable
        if steps_count > 0:
            Q_hat = Qtable[previous['state']][previous['action']]
            Q_hat = Q_hat + (self.alpha * (previous['reward'] + \
                                (self.gamma * (max(Qtable[state].values()))) - Q_hat))
            Qtable[previous['state']][previous['action']] = Q_hat
            # update the entire table in one step
            self.Qtable = Qtable
