# -*- coding: utf-8 -*-
import sys
import numpy as np

ACTIONS = ['left', 'right', 'forward', 'suck', 'off']
DIRTY, CLEAN, WALL = 0, 1, 2
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
velocity_map = [(0, -1), (1, 0), (0, 1), (-1, 0)]
UNICODE_ENABLED = True

character_map = ['D ', '  ', 'W ']
robot_char_map = ['^R', 'R>', 'VR', '<R']
if UNICODE_ENABLED:
    character_map = ['💩 ', '⬛ ', '⬜ ']
    robot_char_map = ['⇧ ', '⇨ ', '⇩ ', '⇦ ']

class VacuumWorld():
    def __init__(self, filename=None):
        # Default to a 10x10 random world
        self.width = 10
        self.height = 10
        # Each cell can be dirty, clean, or wall
        self.grid = np.random.randint(3, size=(self.height, self.width))
        # Start at the bottom-left corner facing upwards
        self.x, self.y = 0, self.height - 1
        self.direction = NORTH
        if filename:
            self.load_from_file(filename)

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
        sys.stdout.write('\n')


    def load_from_file(self, filename):
        lines = list(open(filename).readlines())
        self.height = len(lines)
        self.width = max(len(line) for line in lines)
        self.grid = np.ones((self.height, self.width), int)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == 'W':
                    self.grid[y, x] = WALL
                elif char == 'D':
                    self.grid[y, x] = DIRTY
                elif char == 'S':
                    self.x, self.y = x, y
        self.direction = NORTH
