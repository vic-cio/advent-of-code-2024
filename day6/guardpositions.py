from pathlib import Path
import numpy as np

current_directory = Path(__file__).parent
grid_string = (current_directory / 'gridwithobstacles.txt').read_text()
lab_grid = [[char for char in row] for row in grid_string.split('\n')]

"""Find the guard's position and orientation"""

def findguard(grid):  # Get the guard's position and orientation
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in "^v<>":
                print ("Guard found:", x, y, cell)
                return (x, y, cell)

"""takes coords and grid parameters"""
def inbound(x, y, length, height):  
    print("Inbound? (", x , y, ")", "(", length, height, ")")
    return 0 <= x < length and 0 <= y < height

def next_pos_and_direction(x, y, direction):
    if direction == "^":
        return (x, y - 1, direction)
    elif direction == ">":
        return (x + 1, y, direction)
    elif direction == "v":
        return (x, y + 1, direction)
    elif direction == "<":
        return (x - 1, y, direction)

def path_finder(grid):
    x_len = len(grid[0])
    y_len = len(grid)

    active_grid = [list(row) for row in grid] # Grid to be dynamically updated
    orientations = "^>v<"  # Order of rotations for directions

    initial_state = findguard(active_grid)
    if initial_state is None:
        return "Guard not found"
    
    current_state = initial_state
    active_grid[current_state[1]][current_state[0]] = "X"

    distinct_points = {current_state[:2]}
    print(distinct_points)
    distinct_states = {current_state}
    print(distinct_states)
    print(len(distinct_points))

    # distinct_states.add((4, 7, "^"))
    # if (4, 7, "^") in distinct_states:
    #     return 0

    moves = 0
    while moves < 15000:
        print("Move:", moves)
        next_state = next_pos_and_direction(current_state[0], current_state[1], current_state[2])
        print("trying next state:", next_state)

        if inbound(next_state[0], next_state[1], x_len, y_len):
            next_cell = active_grid[next_state[1]][next_state[0]]
            print("next cell:", next_cell)
        else:
            print("Out of bounds")
            return len(distinct_points), distinct_points
        
        if next_state in distinct_states:
            print("loop detected")
            return 0, set()
        
        elif next_cell == "#":
            print("Obstacle detected")
            next_state = (current_state[0], current_state[1],
                             orientations[(orientations.index(current_state[2]) + 1) % len(orientations)])
    
        elif next_cell == "X":
            print("Visited cell")

        elif next_cell == ".":
            active_grid[next_state[1]][next_state[0]] = "X"
            print("New cell")

        else:
            return ("case not found"), distinct_points
        
        current_state = next_state
        distinct_points.add(current_state[:2])
        distinct_states.add(current_state)

        moves += 1

    return ("out of moves"), distinct_points





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

test_2 = """.#..
.^.#
#...
..#."""

test_grid = [[char for char in row] for row in test_grid_string.split('\n')] #find path
test_grid_2 = [[char for char in row] for row in test_2.split('\n')] #find loop

print(path_finder(test_grid))
print(path_finder(test_grid_2))
print(path_finder(lab_grid)) #find path

