import random
from QLearner import QLearner
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
from random import choice as randomChoice

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # Initialize any additional variables here
        self.steps_count = 0
        self.QTable = QLearner(actions=Environment.valid_actions, gamma=0.35, epsilon=0.85, alpha=0.75)
        self.previous = {'action': None, 'reward': None, 'state': None}

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # Prepare for a new trip; reset any variables here, if required
        self.previous = {'action': None, 'reward': None, 'state': None}
        self.steps_count = 0

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint() # from route planner
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # Update the current state
        self.state = (
            ('directions', self.next_waypoint),
            ('light', inputs['light']),
            ('oncoming', inputs['oncoming']),
        )

        # Select action according to your policy
        action = self.QTable.next_action(state=self.state)

        # Execute action and get reward
        reward = self.env.act(self, action)

        # Update the Q value // Learn policy based on state, action, reward
        self.QTable.update(state=self.state, previous=self.previous, steps_count=self.steps_count)

        # Store actions, state and reward as previous for use in the next cycle
        self.previous['state'] = self.state
        self.previous['action'] = action
        self.previous['reward'] = reward
        self.steps_count += 1

        # Debugging
        print "State: {}".format(self.state)
        print "Action: {}, Reward: {}".format(action, reward)
        print "Q-Values: {}".format(self.QTable.Q_by_state(state=self.state))
        print "-------------------"

    def log_to_file(self, info):
        with open("log.txt", "a") as log_file:
            log_file.write(info)
            log_file.close()


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.1, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
