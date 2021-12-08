#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input
import operator

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

DAY = 3
PUZZLE_INPUT = "https://adventofcode.com/2021/day/{day_number}/input"
INPUT_FILE_PATH = "input.txt"

def solve(data):
    oxygen = calculate_life_support(data, 0, operator.ge)
    CO2 = calculate_life_support(data, 0, operator.lt)

    gamma = "".join(str(x) for x in oxygen)
    epsilon = "".join(str(x) for x in CO2)
    result = int(gamma, 2) * int(epsilon, 2)

    return {"oxygen": oxygen, "CO2": CO2, "result": result}

def calculate_bit_criteria(data, operator):
    total_entries = len(data)
    bit_length = len(data[0])
    sums = [0] * bit_length

    for index in range(bit_length):
        sums[index] = sum(map(lambda item: int(item[index]), data))

    return list(map(lambda x: 1 if operator(x, total_entries/2) else 0, sums))

def calculate_life_support(candidates, index, operator):
    if len(candidates) <= 1 or index >= len(candidates[0]):
        return candidates

    bit_criteria = calculate_bit_criteria(candidates, operator)
    candidates = list(filter(lambda item: int(item[index]) == bit_criteria[index], candidates))

    print("Criteria: " + str(bit_criteria))
    print("Index: " + str(index) + ", Bit: " + str(bit_criteria[index]))
    print("Candidates:" + str(candidates))

    return calculate_life_support(candidates, index + 1, operator)

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
