import numpy as np

ACTIONS = ['left', 'right', 'forward', 'suck', 'off']
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

class VacuumWorld():
    def __init__(self):
        # TODO: init walls
        self.walls = np.array((10,10))
        self.direction = EAST
        self.x, self.y = 0, 0

    def get_percepts(self):
        # There are 3 percepts: a wall sensor = 1 if the machine has a wall right in the front and 0 otherwise
        # a dirt sensor = 1 if the square contains dirt,
        # and a home sensor = 1 if the agent is home (the starting location).
        return {
            'wall': 0,
            'dirt': 1,
            'home': 1,
        }

    def take_action(self, action):
        if action not in ACTIONS:
            raise ValueError("Unknown action")
        pass


class VacuumAgent():
    def __init__(self, environment):
        self.environment = environment

    def act(self):
        pass


class SimpleReflexAgent(VacuumAgent):
    def act(self, environment):
        return 'left'
