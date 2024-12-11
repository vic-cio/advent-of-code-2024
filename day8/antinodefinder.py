from pathlib import Path
import math
from itertools import product

current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'antennaarray.txt' # Join the directory with the file name
array_str = file_path.read_text()