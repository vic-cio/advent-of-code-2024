from pathlib import Path
from collections import Counter

current_directory = Path(__file__).parent # Get the directory of the running python script
file_path = current_directory / 'wordsearch.txt' # Join the directory with the file name
word_search_data = file_path.read_text()

rows = word_search_data.split("\n") # Split the file into lines
word_search = [list(row) for row in rows]


sample_word_search_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# test_rows = sample_word_search_data.split("\n") # Split the test case into lines
# test_word_search = [list(row) for row in test_rows]
# print(test_word_search)

def find_xmas(grid):
    xmas_count = 0
    row_length = len(grid[0])
    col_length = len(grid)

    for i in range(col_length):
        for j in range(row_length):
            if row_length - j >= 4:
                if "".join(grid[i][j:j+4]) in ["XMAS", "SAMX"]:
                    xmas_count += 1
            
            if col_length - i >= 4:
                if "".join([grid[i+k][j] for k in range(4)]) in ["XMAS", "SAMX"]:
                    xmas_count += 1
            
            if row_length - j >= 4 and col_length - i >= 4:
                if "".join([grid[i+k][j+k] for k in range(4)]) in ["XMAS", "SAMX"]:
                    xmas_count += 1

            if j >= 3 and col_length - i >= 4:
                if "".join([grid[i+k][j-k] for k in range(4)]) in ["XMAS", "SAMX"]:
                    xmas_count += 1

    return xmas_count

def find_x_mas(grid):
    x_mas_count = 0
    row_length = len(grid[0])
    col_length = len(grid)
    
    def cross_check(a, b):
        if "".join([grid[a-1+k][b-1+k] for k in range(3)]) in ["MAS", "SAM"]:
            if "".join([grid[a-1+k][b+1-k] for k in range(3)]) in ["MAS", "SAM"]:
                return True

    for i in range(col_length):
        for j in range(row_length):
            if grid[i][j] == "A":
                if row_length - j >= 2 and col_length - i >= 2 and i >= 1 and j >= 1:
                    if cross_check(i, j):
                        x_mas_count += 1
    return x_mas_count

print(find_xmas(word_search))
print(find_x_mas(word_search))