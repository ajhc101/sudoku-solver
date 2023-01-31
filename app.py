import numpy as np
from sudoku_utils import board_print

sudoku = np.array([
    [ 0, 0, 0, 0, 0, 0, 5, 7, 3],
    [ 8, 0, 0, 0, 2, 0, 0, 0, 0],
    [ 7, 0, 0, 9, 0, 0, 8, 1, 0],
    [ 5, 8, 0, 7, 0, 6, 0, 0, 0],
    [ 0, 0, 1, 8, 0, 0, 0, 6, 0],
    [ 2, 3, 0, 0, 4, 0, 0, 0, 9],
    [ 9, 1, 5, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 8, 0, 6, 0, 1],
    [ 0, 0, 0, 0, 0, 0, 0, 4, 0]
])

# return a list of numbers already used in a row
def get_values_in_row(grid, row):
    values_in_row = []

    for number in grid[row, :]:
        if number != 0:
            values_in_row.append(number)

    return values_in_row

# return a list of numbers already used in a column
def get_values_in_column(grid, col):
    values_in_column = []

    for number in grid[:, col]:
        if number != 0:
            values_in_column.append(number)

    return values_in_column

# return a list of numbers already used in a box
def get_values_in_box(grid, row, col):
    top_bound = (row // 3) * 3
    bottom_bound = top_bound + 2
    left_bound = (col // 3) * 3
    right_bound = left_bound + 2
    little_grid = grid[top_bound:(bottom_bound + 1), left_bound:(right_bound + 1)]
    values_in_box = []

    for r in range(0,3):
        for c in range(0,3):
            if little_grid[r][c] != 0:
                values_in_box.append(little_grid[r, c])

    return values_in_box

# return a list of numbers that can be placed in a particular spot 
def get_spot_values(grid, row, col):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    values_in_row = get_values_in_row(grid, row)
    values_in_column = get_values_in_column(grid, col)
    values_in_box = get_values_in_box(grid, row, col)
    possibilities = []

    for number in numbers:
        if (number not in values_in_row) and (number not in values_in_column) and (number not in values_in_box):
            possibilities.append(number)

    return possibilities
