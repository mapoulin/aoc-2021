#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input
from collections import deque
from functools import reduce
import collections

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

class Cave:
    def __init__(self, name, neighbors=[]):
        self.name = name
        self.big = name.isupper()
        self.neighbors = neighbors

    def __eq__(self, other):
        if isinstance(other, Cave):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return str(self.name)

def solve(data):
    cave_system = parse_input(data)
    paths = []

    visit(cave_system["start"], [], paths)

    for path in paths:
        print(path)

    return len(paths)

def visit(current, visited, paths):
    visited.append(current)

    if current.name == "end":
        paths.append(",".join(map(lambda cave: cave.name, visited)))
        return

    visited_counter = collections.Counter(visited)
    already_visited_a_cave_twice = False

    for cave in visited:
        if not cave.big and visited_counter[cave] >= 2:
            already_visited_a_cave_twice = True
            break

    for neighbor in current.neighbors:
        if neighbor.name == "start":
            continue

        if(neighbor.name == "end" or neighbor.big or visited_counter[neighbor] == 0 or \
        (not already_visited_a_cave_twice and visited_counter[neighbor] < 2)):
            visit(neighbor, visited.copy(), paths)

def parse_input(data):
    cave_system = {}

    for line in data:
        paths = line.split("-")

        for path in paths:
            if path not in cave_system:
                cave_system[path] = Cave(path, [])

        cave_system[paths[0]].neighbors.append(cave_system[paths[1]])
        cave_system[paths[1]].neighbors.append(cave_system[paths[0]])

    return cave_system

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
