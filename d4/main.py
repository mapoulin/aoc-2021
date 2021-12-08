#!/usr/bin/env python3

import re
from os.path import dirname, abspath
from aoc_utils import read_input
import numpy as np

DAY = re.search("d([0-9]+)", dirname(abspath(__file__))).group(1) # d[0-9]+ -> [0-9]+

def solve(data):
    parsed = parse_input(data)
    count = 0
    winner_board = np.array([])
    winner_number = 0

    for callout_number in parsed["callout"]:
        for board in parsed["boards"]:
            if validate_board(board):
                continue

            np.ma.masked_where(board == callout_number, board, copy=False)
            print(board)

            if validate_board(board):
                winner_board = board
                winner_number = callout_number

    return np.sum(winner_board) * winner_number


def validate_board(board):
    (row_count, column_count) = board.shape

    row_win = any(map(lambda count: row_count == count, np.ma.count_masked(board, axis=1)))
    column_win = any(map(lambda count: column_count == count, np.ma.count_masked(board, axis=0)))

    return row_win or column_win

def parse_input(data):
    callout = list(map(int, data[0].split(",")))
    boards = []
    current_board = []

    for index in range(2, len(data)):
        if (data[index] == ""):
            boards.append(np.ma.MaskedArray(current_board, mask=False))
            current_board = []
            continue

        row = list(map(int, filter(None, data[index].split(" "))))
        current_board.append(row)

    return {"callout": callout, "boards": boards}

if __name__ == "__main__":
    puzzle_input = read_input(DAY)
    solution = solve(puzzle_input)
    print(solution)
