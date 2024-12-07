from pathlib import Path

current_directory = Path(__file__).parent
grid_string = (current_directory / 'gridwithobstacles.txt').read_text()

grid = [[char for char in row] for row in grid_string.split('\n')]

print(grid)
