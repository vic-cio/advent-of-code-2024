from pathlib import Path
import re


current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'scrambledfunctions.md' # Join the directory with the file name
scrambled_string = file_path.read_text()
pattern = r"mul\(\d+,\d+\)"
found_functions = re.findall(pattern, scrambled_string)

# test_case = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))" # Test case
# found_test = re.findall(pattern, test_case)

mul = lambda x,y: int(x) * int(y)
running_total = sum([eval(func) for func in found_functions])
print(running_total)
