import numpy as np
import environments
from environments import ACTIONS

# LeftBot is a deterministic reflex agent
# It is computationally efficient, and can be implemented in hardware
class LeftBot():
    def act(self, percepts):
        return 'left'


# RandomBot provably cleans any room. Given enough time.
class RandomBot():
    def act(self, percepts):
        return np.random.choice(['suck', 'left', 'forward'])


# Scores 100% on the Turing test
class HumanBot():
    def act(self, percepts):
        print('Actions: {}'.format(ACTIONS))
        return raw_input('Select an action: ')


# The first agent for the assignment
class SimpleReflexAgent():
    def act(self, percepts):
        if percepts['dirt']:
            return 'suck'
        if percepts['wall']:
            return 'left'
        return 'forward'


# The second agent for the assignment
class RandomizedReflexAgent():
    def act(self, percepts):
        if percepts['dirt']:
            return 'suck'
        if percepts['wall']:
            return np.random.choice(['left', 'right'])
        if np.random.random() > 0.25:
            return 'forward'
        return 'right'
        
        
#DeterministicModelBasedReflexAgent
class DMBRA():
    def __init__(self):
        self.state = 0
    
    
    def act(self, percepts):
        wall = percepts['wall']
        home = percepts['home']
        print("state is : " + str(self.state))
    
        if percepts['dirt']:
            return 'suck'
        if self.state == 0:
            if wall:
                self.state = 1
                return 'right'
            else:
                return 'forward'
        if self.state == 1:
            if wall:
                return 'right'
            else:
                self.state = 2
                return 'forward'
        if self.state == 2:
            self.state = 3
            return 'right'
        if self.state == 3:
            if wall:
                self.state = 4
                return 'left'
            else:
                return 'forward'
        if self.state == 4:
            if wall:
                return 'left'
            else:
                self.state = 5
                return 'forward'
        if self.state == 5:
            self.state = 0
            return 'left'
        
        raise ValueError("Unknown State")


# The third agent for the assignment
class ModelBasedAgent():
    def act(self, percepts):
        # TODO: Implement
        return 'forward'
