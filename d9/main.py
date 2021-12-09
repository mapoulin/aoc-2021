#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

class Tile:
    def __init__(self, heatmap, index, value):
        self.heatmap = heatmap
        self.index = index
        self.value = value
        self.seen = False

    # neighbors
    def up(self):
        return self.heatmap[self.index[0] - 1][self.index[1]] if(self.index[0] > 0) else None
    def left(self):
        return self.heatmap[self.index[0]][self.index[1] - 1] if(self.index[1] > 0) else None
    def down(self):
        return self.heatmap[self.index[0] + 1][self.index[1]] if(self.index[0] < len(self.heatmap) - 1) else None
    def right(self):
        return self.heatmap[self.index[0]][self.index[1] + 1] if(self.index[1] < len(self.heatmap[self.index[0]]) - 1) else None

    def __repr__(self):
        return str(self.index)

def solve(data):
    heatmap = parse_input(data)
    low_points = []

    for row_index in range(len(heatmap)):
        for column_index in range(len(heatmap[row_index])):
            current = heatmap[row_index][column_index]
            neighbors = [current.up(), current.left(), current.down(), current.right()]
            neighbor_lower = []

            for neighbor in neighbors:
                if(neighbor is not None):
                    neighbor_lower.append(neighbor.value <= current.value)

            if(not any(neighbor_lower)):
                low_points.append(current)

    print(low_points)

    sizes = []
    for low_point in low_points:
        print("Computing bassin " + str(low_point.index))
        size = bassin_size(low_point)
        sizes.append(size)
        print("Size: " + str(size))

    list.sort(sizes, reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def bassin_size(tile):
    if(tile.value == 9):
        tile.seen = True
        return 0

    neighbors_total = 0
    neighbors = [tile.up(), tile.left(), tile.down(), tile.right()]
    for neighbor in neighbors:
        if(neighbor is not None and neighbor.seen is False and neighbor.value > tile.value):
            neighbors_total += bassin_size(neighbor)
            neighbor.seen = True

    return neighbors_total + 1

def parse_input(data):
    heatmap = []

    for row_index in range(len(data)):
        row = []
        heatmap.append(row)
        for column_index in range(len(data[row_index])):
            tile = Tile(heatmap, (row_index, column_index), int(data[row_index][column_index]))
            row.append(tile)

    return heatmap

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
