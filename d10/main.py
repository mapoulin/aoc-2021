#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input
from collections import deque
from functools import reduce

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+
CHUNK_PAIRS = {'[': ']', '(': ')', '{': '}', '<': '>'}
PART_1_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
PART_2_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}

def solve(data):
    scores = []

    for line in data:
        stack = deque()
        invalid = False

        for char in line:
            if char in CHUNK_PAIRS:
                stack.append(char)
            else:
                top = stack.pop()
                if char != CHUNK_PAIRS[top]:
                    print("Expected " + CHUNK_PAIRS[top] + ", but found " + char + " instead.")
                    invalid = True
                    break

        if not invalid:
            missing = []
            while stack:
                missing.append(CHUNK_PAIRS[stack.pop()])
            print("Complete by adding " + "".join(missing))
            scores.append(reduce(lambda counter, char: counter * 5 + PART_2_POINTS[char], missing, 0))

    list.sort(scores, reverse=True)
    return scores[int(len(scores) / 2)]

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
