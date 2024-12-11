from pathlib import Path
import math
from itertools import combinations

current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'antennaarray.txt' # Join the directory with the file name
array_str = file_path.read_text()

rows = array_str.split("\n") 
antenna_array = [list(row) for row in rows]

def map_antennas(array):
    antenna_points = set()
    antenna_map = {}
    for i in range(len(array)):
        for j in range(len(array[0])):
            item = array[i][j]
            if item != ".":
                antenna_points.add((i, j))
                antenna_map.setdefault(item, []).append((i, j))
    return antenna_map, antenna_points

def discover_antinodes(points, max_rows, max_cols):
    x_antinodes = set()
    antenna_pairs = combinations(points, 2)
    
    for pair in antenna_pairs:
        d_row = pair[1][0] - pair[0][0] # Vector generation
        d_col = pair[1][1] - pair[0][1]

        # Generate all positions along the line, extending in both directions
        row, col = pair[0]
        while 0 <= row < max_rows and 0 <= col < max_cols:
            x_antinodes.add((row, col))
            row -= d_row
            col -= d_col

        row, col = pair[1]
        while 0 <= row < max_rows and 0 <= col < max_cols:
            x_antinodes.add((row, col))
            row += d_row
            col += d_col
    
    return x_antinodes

# def discover_antinodes(points, max_rows, max_cols): # Part 1
#     x_antinodes = set()
#     antenna_pairs = combinations(points, 2)
    
#     for pair in antenna_pairs:
#         # Calculate the row and column difference (vector)
#         d_row = pair[1][0] - pair[0][0]
#         d_col = pair[1][1] - pair[0][1]

#         antinode_1 = (pair[0][0] - d_row, pair[0][1] - d_col)
#         antinode_2 = (pair[1][0] + d_row, pair[1][1] + d_col)

#         # Add valid antinodes to the set
#         if 0 <= antinode_1[0] < max_rows and 0 <= antinode_1[1] < max_cols:
#             x_antinodes.add(antinode_1)
        
#         if 0 <= antinode_2[0] < max_rows and 0 <= antinode_2[1] < max_cols:
#             x_antinodes.add(antinode_2)
    
#     return x_antinodes

def find_antinodes(antenna_map, antenna_points, antenna_array):
    max_rows = len(antenna_array)
    max_cols = len(antenna_array[0])
    antinodes = set()
    for antenna_type, points in antenna_map.items(): # Antenna type may be used later
        x_antinodes = discover_antinodes(points, max_rows, max_cols)
        antinodes.update(x_antinodes)

    # antinodes = antinodes - antenna_points # Thought I needed to remove overlaps with antennas
    return antinodes


# example_array_str = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

# example_rows = example_array_str.split("\n")
# example_antenna_array = [list(row) for row in example_rows]

# example_map, example_points = map_antennas(example_antenna_array)

# print(example_map)
# print(find_antinodes(example_map, example_points, example_antenna_array))
# print(len(find_antinodes(example_map, example_points, example_antenna_array)))

task_map, task_points = map_antennas(antenna_array)
antinodes = find_antinodes(task_map, task_points, antenna_array)
print(len(antinodes))

# example_array_with_antinodes = [] # Debug: Print the array with antinodes

# for i in range(len(example_antenna_array)):
#     row = example_antenna_array[i]
#     new_row = []
#     for j in range(len(row)):
#         if (i, j) in find_antinodes(example_map, example_points, example_antenna_array):
#             new_row.append("X")
#         else:
#             new_row.append(row[j])
#     example_array_with_antinodes.append(new_row)

# print("\n".join(["".join(row) for row in example_array_with_antinodes]))

"""
......X....X
...X....0...
....X0....X.
..X....0....
....0....X..
.X....A.....
...X........
X......X....
........A...
.........A..
..........X.
..........X.
"""

"""
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
"""