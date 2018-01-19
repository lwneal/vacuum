# -*- coding: utf-8 -*-
import sys
import numpy as np

ACTIONS = ['left', 'right', 'forward', 'suck', 'off']
DIRTY, CLEAN, WALL = 0, 1, 2
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
velocity_map = [(0, -1), (1, 0), (0, 1), (-1, 0)]

ascii_character_map = ['D ', '  ', 'W ']
ascii_robot_char_map = ['^R', 'R>', 'VR', '<R']

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
        self.timestep = 0
        if filename:
            self.load_from_file(filename)
        self.home_x, self.home_y = self.x, self.y
        self.initial_dirt = (self.grid == DIRTY).sum()

    def get_percepts(self):
        # There are 3 percepts:
        # a wall sensor = 1 if facing a wall, 0 otherwise
        # a dirt sensor = 1 if the current square is dirty,
        # a home sensor = 1 if the current square is the starting location
        return {
            'wall': self.hits_wall(),
            'dirt': self.grid[self.y, self.x] == DIRTY,
            'home': self.x == self.home_x and self.y == self.home_y,
        }
    
    def hits_wall(self):
        dx, dy = velocity_map[self.direction]
        new_x, new_y = self.x + dx, self.y + dy
        if not 0 < new_x < self.width:
            return True
        if not 0 < new_y < self.height:
            return True
        return self.grid[new_y, new_x] == WALL

    def update(self, action):
        self.timestep += 1
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
            if not self.hits_wall():
                self.x += dx
                self.y += dy
        else:
            raise ValueError("Unknown action {}".format(action))
        

    def print_state(self, csv_mode=False, time_to_90_mode=False):
        num_dirt = (self.grid == DIRTY).sum()
        if csv_mode:
            sys.stdout.write("{},{}\n".format(self.timestep, num_dirt))
            return
        elif time_to_90_mode:
            dirtiness = float(num_dirt) / (self.initial_dirt)
            if dirtiness <= 0.1:
                print(self.timestep)
                sys.exit()
            return
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
        self.width = max(len(line) for line in lines) - 1
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
