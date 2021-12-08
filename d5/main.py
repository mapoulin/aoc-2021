#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input
from functools import reduce
import numpy as np

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

def solve(data):
    coordinates = parse_input(data)

    shape = (reduce(max, flatMap(lambda coord: coord[1], coordinates)) + 1,
             reduce(max, flatMap(lambda coord: coord[0], coordinates)) + 1)

    terrain = np.zeros(shape)

    for coords in coordinates:
        for point in expand_coords(coords):
            np.add.at(terrain, point, 1)

    return np.count_nonzero(terrain >= 2)

def expand_coords(c):
    min_x, max_x = min(c[0][0], c[1][0]), max(c[0][0], c[1][0])
    min_y, max_y = min(c[0][1], c[1][1]), max(c[0][1], c[1][1])

    if min_x == max_x:
        return [(y, min_x) for y in range(min_y, max_y + 1)]

    slope = (c[1][1] - c[0][1]) / (c[1][0] - c[0][0])
    b = c[0][1] - slope * c[0][0]

    return [(int(slope * x + b), x) for x in range(min_x, max_x + 1)]

def parse_input(data):
    return [[tuple(map(int, coords.split(","))) for coords in line.split(" -> ")] for line in data]

def flatMap(function, array):
    return map(function, reduce(list.__add__, array))

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
