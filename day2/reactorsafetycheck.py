from pathlib import Path

current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'rednosereactorlevels.md' # Join the directory with the file name
levels_data = file_path.read_text() # Read file
# print(levelsdata) # Debug

levels_list = levels_data.split("\n") # Split the file into lines

"""Checks to see whether a sequence of levels is fully safe"""
def is_safe(levels):
    is_increasing = all(x < y and abs(x - y) <= 3 for x, y in zip(levels, levels[1:]))
    is_decreasing = all(x > y and abs(x - y) <= 3 for x, y in zip(levels, levels[1:]))
    return is_increasing or is_decreasing

"""Checks to see whether a sequence of levels is mostly safe"""
def is_mostly_safe(levels):
    if max(is_safe(levels)): # If the levels are fully safe, return True
        return True

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]  # Remove the offending element
        if is_safe(modified_levels):
            return True
        
    return False


"""testing ground"""
test_data = [[7,6,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
print(sum([is_mostly_safe(entry) for entry in test_data]))
print(is_mostly_safe([7,6,4,2,1]))



# safe_reports = sum([is_safe(list(map(int, entry.split(" ")))) for entry in levels_list])
# mostly_safe_reports = sum([is_mostly_safe(list(map(int, entry.split(" ")))) for entry in levels_list])

# print(safe_reports)
# print(mostly_safe_reports)


# """old clumsy way of reading file"""
# import os
# current_directory = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_directory, 'rednosereactorlevels.md')

# with open(file_path, 'r') as file:
#     levelsdata = file.read()

# print(levelsdata)