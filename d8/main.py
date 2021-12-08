#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input
from functools import reduce

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

def solve(data):
    return reduce(lambda counter, line: counter + solve_line(line), parse_input(data), 0)

def solve_line(line):
    numbers = {
        frozenset(["a", "b", "c", "e", "f", "g"]) :         "0",
        frozenset(["c", "f"]):                              "1",
        frozenset(["a", "c", "d", "e", "g"]):               "2",
        frozenset(["a", "c", "d", "f", "g"]):               "3",
        frozenset(["b", "c", "d", "f"]):                    "4",
        frozenset(["a", "b", "d", "f", "g"]):               "5",
        frozenset(["a", "b", "d", "e", "f", "g"]):          "6",
        frozenset(["a", "c", "f"]):                         "7",
        frozenset(["a", "b", "c", "d", "e", "f", "g"]):     "8",
        frozenset(["a", "b", "c", "d", "f", "g"]):          "9"
    }
    length_map = [[] for _ in range(8)]
    letters = {}

    for code in line[0]:
        length_map[len(code)].append(code)

    # a
    letters["a"] = set(length_map[3][0]).difference(set(length_map[2][0])).pop()
    # d
    b_d = set(length_map[4][0]).difference(set(length_map[2][0]))
    letters["d"] = list(filter(lambda x: len(x), map(lambda x: set(b_d).difference(x), length_map[6])))[0].pop()
    # b
    letters["b"] = set(b_d).difference(letters["d"]).pop()
    # e
    e_g = set(length_map[7][0]).difference(set(length_map[4][0])).difference(set(length_map[3][0]))
    letters["e"] = list(filter(lambda x: len(x), map(lambda x: set(e_g).difference(x), length_map[6])))[0].pop()
    # g
    letters["g"] = set(e_g).difference(letters["e"]).pop()
    # c
    letters["c"] = list(filter(lambda x: len(x), map(lambda x: set(length_map[2][0]).difference(x), length_map[6])))[0].pop()
    # f
    letters["f"] = set(length_map[2][0]).difference(letters["c"]).pop()

    letters = dict((v,k) for k,v in letters.items()) # invert key / values
    unscrambled = list(map(lambda word: frozenset([letters[l] for l in word]), line[1]))
    digits = list(map(lambda segments: numbers[segments], unscrambled))

    return int("".join(digits))

def parse_input(data):
    return [[[w for w in seg.split(" ")] for seg in line.split(" | ")] for line in data]

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
