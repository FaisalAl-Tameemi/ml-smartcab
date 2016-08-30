import random

class QLearner():
    """A QTable Implementation"""

    def __init__(self, actions, Q_init=2, gamma=0.8):
        self.ACTIONS = actions
        self.QTable = {}
        self.Q_init = Q_init  #initial Q^ values for new state-actions not observed yet.
        self.gamma = gamma  #discounting rate of future rewards
        # self.epsilon = 0.75 + (0.24 / (1+( math.exp(-0.1*(self.learn_count-40)))))
        # self.alpha = 1 - ( 0.5 / (1 + math.exp(-0.05*(self.learn_count-100)))) #alpha ranges from 1 to 0.5
        self.epsilon = 0.5
        self.alpha = 0.5


    def next_action(self, state):
        if self.QTable.has_key(state):  #check if state has been encountered before or not
            # If epsilon is not eclipsed by a random float, then choose the action with the largest Q^.
            # If epsilon is 1, then best option is always chosen as it cannot be eclipsed
            if random.random() < self.epsilon :
                # pull the best action, or best actions if there are more than one with a max Q^ value
                argmax_actions = {action:Qhat for action, Qhat in self.QTable[state].items() \
                                    if Qhat == max(self.QTable[state].values())}
                # note if only 1 action in this list, then it is only choice for random.choice
                return random.choice(argmax_actions.keys())
            else: # if random float eclipses epsilon, choose a random action.
                return random.choice(self.ACTIONS)
        else:  #state has never been encountered
            #Add state to Qtable dictionary
            self.QTable.update({
                state: {None: self.Q_init, 'forward': self.Q_init, 'left': self.Q_init, 'right': self.Q_init}
            })
            #choose one of the actions at random
            return random.choice(self.ACTIONS)


    def update(self, state, previous, steps_count):
        Qtable = self.QTable
        if steps_count > 0 :  #make sure it is not the first step in a trial.
            Q_hat = Qtable[previous['state']][previous['action']]
            Q_hat = Q_hat + (self.alpha * (previous['reward'] + \
                                (self.gamma * (max(Qtable[state].values()))) - Q_hat))
            Qtable[previous['state']][previous['action']] = Q_hat
            # update the entire table in one step
            self.Qtable = Qtable
