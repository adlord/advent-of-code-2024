import sys
import os

try:
    from utils import measure_time
except ImportError:
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, project_root)
    from utils import measure_time

CURRENT_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(CURRENT_DIR, "input.txt")


@measure_time
def count_xmas(input_file):

    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f]

        num_rows = len(grid)
        num_cols = len(grid[0])
        occurrence_count = 0

        def match_word(
                target_word,
                start_row,
                start_col,
                row_increment,
                col_increment):
            target_length = len(target_word)

            for i in range(target_length):
                current_row = start_row + i * row_increment
                current_col = start_col + i * col_increment
                within_bounds = (
                    0 <= current_row < num_rows and 0 <= current_col < num_cols
                )
                if not within_bounds or (
                    grid[current_row][current_col] != target_word[i]
                ):
                    return False

            return True

        for row in range(num_rows):
            for col in range(num_cols):
                directions = [
                    (1, 1),  # Down-right diagonal
                    (-1, 1),  # Up-right diagonal
                ]

                if match_word(
                    "MAS", row, col, directions[0][0], directions[0][1]
                ) or match_word(
                        "SAM", row, col, directions[0][0], directions[0][1]):
                    if match_word(
                        "MAS", row + 2, col, directions[1][0], directions[1][1]
                    ) or match_word(
                        "SAM", row + 2, col, directions[1][0], directions[1][1]
                    ):
                        occurrence_count += 1
        return occurrence_count


if __name__ == "__main__":
    try:
        result = count_xmas(INPUT_FILE)
        print(result)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
