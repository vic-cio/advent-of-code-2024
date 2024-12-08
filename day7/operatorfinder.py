from pathlib import Path

current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'calibrationvalues.txt' # Join the directory with the file name
calibration_str = file_path.read_text()

print(calibration_str) 