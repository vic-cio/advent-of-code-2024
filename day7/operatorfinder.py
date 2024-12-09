from pathlib import Path
import math
from itertools import product

current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'calibrationvalues.txt' # Join the directory with the file name
calibration_str = file_path.read_text()

lines = calibration_str.split("\n")
parsed_data = [line.split(":") for line in lines]

"""Array of lists containing the target value and an array of components
   e.g. [[target_1, [component1a, component1b, ...]], ...]"""

calibration_values = [[int(targ), [int(x) for x in comp.strip().split()]] for targ, comp in parsed_data]

# print(len(calibration_values)) # Number of calibration values
# print(calibration_values[100]) # First calibration value


def generate_operator_combinations(components):
    operator_count = len(components) - 1
    operators = ['+', '*', '||']
    operator_combinations = list(product(operators, repeat=operator_count))
    return operator_combinations

# def factor_check(target, addends, factors):
#     if not addends or not factors:
#         return False
    
#     sum_addends = sum(addends)
#     product_factors = math.prod(factors)

#     if product_factors > target - sum_addends:
#         return False

#     if (target - sum_addends) % product_factors == 0:
#         print(f"Target: {target}, Sum of rems: {sum_addends}, Product of factors: {product_factors}")
#         return True
    
#     return False

def is_possible_value(target, components):
    if not components:
        return 0
    
    operator_combinations = generate_operator_combinations(components)
    operator_map = {'+': lambda x, y: x + y, '*': lambda x, y: x * y, '||': lambda x, y: int(str(x) + str(y))}

    for op_comb in operator_combinations:
        running_total = components[0]
        for i in range(len(op_comb)):
            running_total = operator_map[op_comb[i]](running_total, components[i + 1])
            if running_total > target:
                continue
        if running_total == target:
            return target

    return 0
# print(is_possible_value(20, [10, 10])) # 20
# print(is_possible_value(25, [10, 10, 10, 10])) # 20


# test_case = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

# test_list = test_case.split("\n")
# test_data = [line.split(":") for line in test_list]
# test_values = [[int(targ), [int(x) for x in comp.strip().split()]] for targ, comp in test_data]

# test_sum_values = 0
# for input in test_values:
#     test_sum_values += is_possible_value(input[0], input[1])

# print(test_sum_values)

sum_values = 0
for input in calibration_values:
    sum_values += is_possible_value(input[0], input[1])

print(sum_values)