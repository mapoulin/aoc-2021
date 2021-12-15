#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input
from collections import deque
from functools import reduce

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

class Octopus:
    def __init__(self, grid, index, energy):
        self.grid = grid
        self.index = index
        self.energy = energy
        self.flashed = False

    def neighbor(self, row, column):
        if(self.index[0] + row < 0 or self.index[0] + row >= len(self.grid)):
            return None

        if(self.index[1] + column < 0 or self.index[1] + column >= len(self.grid[self.index[0]])):
            return None

        return self.grid[self.index[0] + row][self.index[1] + column]

    def neighbors(self):
        neighbors = [
            self.neighbor(-1, 0),    # up
            self.neighbor(0, -1),    # left
            self.neighbor(1, 0),     # down
            self.neighbor(0, 1),     # right
            self.neighbor(-1, -1),   # up_left
            self.neighbor(-1, 1),    # up_right
            self.neighbor(1, -1),    # down_left
            self.neighbor(1, 1),     # down_right
        ]

        return list(filter(None, neighbors))

    def __repr__(self):
        return str(self.index)

def solve(data):
    grid = parse_input(data)
    round_number = 0
    all_flashed = False

    while not all_flashed:
        round_number += 1
        all_flashed = True

        # Step 1
        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])):
                octopus = grid[row_index][column_index]
                octopus.energy += 1
        # Step 2
        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])):
                octopus = grid[row_index][column_index]
                process_flash(octopus)
        # Step 3
        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])):
                octopus = grid[row_index][column_index]
                all_flashed &= octopus.flashed
                if(octopus.flashed):
                    octopus.energy = 0
                    octopus.flashed = False

    return round_number

def process_flash(octopus):
    if(octopus.energy > 9 and octopus.flashed is False):
        octopus.flashed = True
        for neighbor in octopus.neighbors():
            neighbor.energy += 1
            process_flash(neighbor)

def parse_input(data):
    grid = []

    for row_index in range(len(data)):
        row = []
        grid.append(row)
        for column_index in range(len(data[row_index])):
            octopus = Octopus(grid, (row_index, column_index), int(data[row_index][column_index]))
            row.append(octopus)

    return grid


if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
