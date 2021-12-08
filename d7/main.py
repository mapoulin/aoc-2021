#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input
import statistics

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

def solve(data):
    coordinates = parse_input(data)
    median = int(statistics.median(coordinates))

    left_gas = compute_gas(coordinates, median)
    right_gas = compute_gas(coordinates, median+1)
    position = median

    while left_gas >= right_gas:
        position = position + 1
        left_gas = right_gas
        right_gas = compute_gas(coordinates, position)
       # print(right_gas)

    while left_gas < right_gas:
        position = position - 1
        right_gas = left_gas
        left_gas = compute_gas(coordinates, position)
        #print(left_gas)

    return {"median": median, "position": position, "fuel": min(left_gas, right_gas)}

def compute_gas(coordinates, w):
    fuel = 0
    for value in coordinates:
        step = int(abs(value - w) * (abs(value - w) + 1) / 2)
        #print("Move from " + str(value) + " to " + str(w) + ": " + str(step) + " fuel")
        fuel += step
    return fuel

def parse_input(data):
    return [int(x) for x in data[0].split(",")]

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
