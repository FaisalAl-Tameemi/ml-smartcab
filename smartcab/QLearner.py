import random

class QLearner():
    """
    A QTable Implementation

    Allows the smartcab agent to store it's previous states and learn from the
    actions it has taken in the past to maximize its reward in the future.
    """

    def __init__(self, actions, Q_init=2, gamma=0.5, epsilon=0.5, alpha=0.5):
        self.ACTIONS = actions
        self.QTable = {}
        self.Q_init = Q_init # initial `Q_hat` value arbitrarily
        self.gamma = gamma # discounting rate
        self.epsilon = epsilon # exploration rate
        self.alpha = alpha # learning rate


    def next_action(self, state):
        """
        Get the next best action according to the policy given a state.

        If we have seen this state before, then we simply load the highest Q value
        from the QTable. Otherwise, we will simply add the state to the QTable (Q_init as value for all actions)
        and then take a random action.
        """
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
            # add the state into our QTable with Q_init values for all actions
            self.QTable.update({
                state: { None: self.Q_init, 'forward': self.Q_init, \
                        'left': self.Q_init, 'right': self.Q_init }
            })
            # then choose a random action
            return random.choice(self.ACTIONS)


    def update(self, state, previous, steps_count):
        """
        Update the QTable based on the action taken and the
        reward assigned to that action.

        This function is the one that allows the agent to "learn" by gaining
        experience about the environment.
        """
        if steps_count > 0:
            Q_hat = self.Qtable[previous['state']][previous['action']]
            Q_hat = Q_hat + (self.alpha * (previous['reward'] + \
                                (self.gamma * (max(self.Qtable[state].values()))) - Q_hat))
            self.Qtable[previous['state']][previous['action']] = Q_hat
