#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

def solve(data):
    timers = parse_input(data)

    buckets = [0] * 9
    for timer in timers:
        buckets[timer] += 1

    print("Initial state: " + str(buckets))

    for day in range(256):
        bucket_0 = buckets[0]

        for index in range(len(buckets) - 1):
            buckets[index] = buckets[index+1]

        if bucket_0 > 0:
            buckets[6] += bucket_0
            buckets[8] = bucket_0
        else:
            buckets[8] = 0

        #print("After \t" + str(day + 1) + " days: " + str(buckets))

    return sum(buckets)

def parse_input(data):
    return list(map(int, data[0].split(",")))

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
