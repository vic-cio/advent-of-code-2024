from pathlib import Path

current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'wordsearch.txt' # Join the directory with the file name
word_search_data = file_path.read_text()