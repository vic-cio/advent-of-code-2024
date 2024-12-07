from pathlib import Path
import numpy as np

current_directory = Path(__file__).parent
grid_string = (current_directory / 'gridwithobstacles.txt').read_text()

grid = [[char for char in row] for row in grid_string.split('\n')]

def path_finder(grid):
    """Find the guard's position and orientation"""
    def findguard(grid):  # Get the guard's position and orientation
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell in "^v<>":
                    return (x, y, cell)
        return None  # Guard not found

    def inbound(coords):  # Coords aren't outside the grid
        x, y = coords
        return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

    def next_pos_and_direction(current_state):
        x, y, direction = current_state
        if direction == "^":
            return (x, y - 1, direction)
        elif direction == ">":
            return (x + 1, y, direction)
        elif direction == "v":
            return (x, y + 1, direction)
        elif direction == "<":
            return (x - 1, y, direction)

    orientations = "^>v<"  # Order of rotations for directions

    # Mutable representation of the grid
    active_grid = [list(row) for row in grid]
    initial_state = findguard(active_grid)
    if initial_state is None:
        return "Guard not found"

    current_state = initial_state
    distinct_points = {current_state[:2]}
    active_grid[current_state[1]][current_state[0]] = "X"  # Mark visited

    while True:
        next_state = next_pos_and_direction(current_state)

        if not inbound(next_state[:2]):
            return len(distinct_points)

        next_x, next_y, next_direction = next_state
        next_cell = active_grid[next_y][next_x]

        if next_cell == ".":  # Move forward
            distinct_points.add((next_x, next_y))
            active_grid[next_y][next_x] = "X"
            current_state = next_state

        elif next_cell == "X":  # Continue moving forward
            current_state = next_state

        elif next_cell == "#":  # Turn right
            current_direction = current_state[2]
            new_direction = orientations[(orientations.index(current_direction) + 1) % len(orientations)]
            current_state = (current_state[0], current_state[1], new_direction)

    return "Move limit exceeded"


# print(path_finder(grid))

# """So ugly :("""
# print(sum([
#     sum(
#         path_finder(grid, (x, y)) 
#         for x in range(len(grid[0]))
#     ) 
#     for y in range(len(grid))
# ]))




# Test case
test_grid_string = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

test_grid = [[char for char in row] for row in test_grid_string.split('\n')]

print(path_finder(test_grid))

# """So ugly :("""
# print(sum([
#     sum(
#         path_finder(test_grid, (x, y)) 
#         for x in range(len(test_grid[0]))
#     ) 
#     for y in range(len(test_grid))
# ]))