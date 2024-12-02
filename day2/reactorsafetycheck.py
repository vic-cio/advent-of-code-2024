import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'rednosereactorlevels.md')
# directory = "/Users/victorciobanu/Documents/Programming/advent-of-code-2024/day2"
# os.chdir(directory)
# file_path = 'rednosereactorlevels.md'

with open(file_path, 'r') as file:
    levelsdata = file.read()


print(levelsdata)