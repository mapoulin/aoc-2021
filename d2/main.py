#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

def solve(data):
    horizontal = 0
    depth = 0
    aim = 0

    for item in data:
        value = int(item.split(" ")[1])
        if item.startswith("forward"):
            horizontal += value
            depth += aim * value
        elif item.startswith("down"):
            aim += value
        elif item.startswith("up"):
            aim -= value

    result = horizontal * depth
    return {"horizontal": horizontal, "depth": depth, "aim": aim, "result": result}

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
