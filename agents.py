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
        return np.random.choice(ACTIONS)


# Scores 100% on the Turing test
class HumanBot():
    def act(self, percepts):
        print('Actions: {}'.format(ACTIONS))
        return raw_input('Select an action: ')

