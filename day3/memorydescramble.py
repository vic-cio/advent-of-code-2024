from pathlib import Path
import re

current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'scrambledfunctions.md' # Join the directory with the file name
scrambled_string = file_path.read_text()

patterns = [r"mul\(\d+,\d+\)", r"do\(\)", r"don\'t\(\)"]
patterns_merged = "|".join(patterns)
# pattern = r"mul\(\d+,\d+\)" # Part 1

# test_case = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))" # Test case
# found_test = re.findall(pattern, test_case)
# new_test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)" # Test case part 2
# new_found = re.findall(patterns_merged, new_test)

mul_active = True
mul = lambda x,y: int(x) * int(y)

found_functions = re.findall(patterns_merged, scrambled_string)
running_total = 0

for func in found_functions: #Iterate through the found functions, add the result to the running total if active
    if "mul" in func and mul_active :
        running_total += eval(func)
    elif func == "do()":
        mul_active = True
    elif func == "don't()":
        mul_active = False
    else:
        pass

# running_total = sum([eval(func) for func in new_fixed]) # Part 1

print(running_total)
