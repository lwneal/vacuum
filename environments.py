import sys
import numpy as np

DIRTY, CLEAN, WALL = 0, 1, 2
#character_map = ['D ', '  ', 'W ']
character_map = ['\xf0\x9f\x92\xa9 ', '\xe2\xac\x9b ', '\xe2\xac\x9c ']
robot_char_map = ['\xe2\x87\xa7 ', '\xe2\x87\xa8 ', '\xe2\x87\xa9 ', '\xe2\x87\xa6 ']

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
velocity_map = [(0, -1), (1, 0), (0, 1), (-1, 0)]

ACTIONS = ['left', 'right', 'forward', 'suck', 'off']


def move(position, direction):
    return position + velocity_map[direction]


class VacuumWorld():
    width = 10
    height = 10
    def __init__(self):
        # Each cell can be dirty, clean, or wall
        self.grid = np.random.randint(3, size=(self.height, self.width))
        # Start the the bottom-left corner facing upwards
        self.x, self.y = 0, self.height - 1
        self.direction = NORTH

    def get_percepts(self):
        # There are 3 percepts:
        # a wall sensor = 1 if facing a wall, 0 otherwise
        # a dirt sensor = 1 if the current square is dirty,
        # a home sensor = 1 if the current square is the starting location
        return {
            'wall': 0,
            'dirt': 1,
            'home': 1,
        }

    def update(self, action):
        print(action)
        if action == 'off':
            pass
        elif action == 'suck':
            self.grid[self.y, self.x] = CLEAN
        elif action == 'right':
            self.direction = (self.direction + 1) % 4
        elif action == 'left':
            self.direction = (self.direction - 1) % 4
        elif action == 'forward':
            dx, dy = velocity_map[self.direction]
            new_x = np.clip(self.x + dx, 0, self.width - 1)
            new_y = np.clip(self.y + dy, 0, self.height - 1)
            if self.grid[new_y, new_x] != WALL:
                self.x, self.y = new_x, new_y
        else:
            raise ValueError("Unknown action {}".format(action))
        

    def print_state(self):
        for i, line in enumerate(self.grid):
            for j, square in enumerate(line):
                if (j, i) == (self.x, self.y):
                    sys.stdout.write(robot_char_map[self.direction])
                else:
                    sys.stdout.write(character_map[square])
            sys.stdout.write('\n')
        print(self.grid)
        print("Direction: {}".format(self.direction))
        print('Position: ({}, {})'.format(self.x, self.y))
