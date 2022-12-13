"""Solve Sudoku using backtracking algorithm"""
import copy
from pprint import pprint

from src.helpers.cube_locations_mapping import ALL_XYS
from src.helpers.verifiers import check_solution
from src import example_problems

LAST_KNOWN_GOOD_SOLUTION = []


def check_insert(
    sudoku_square: list[list[int]], x: int, y: int, val_to_insert: int
) -> list[list[int]]:
    """
    Check if inserting `val_to_insert` into position x row, y column
    is going to yield a valid sudoku block. Incomplete is valid too.
    """

    new_sudoku_square = copy.deepcopy(sudoku_square)
    new_sudoku_square[x][y] = val_to_insert

    return check_solution(new_sudoku_square)


def solve(sudoku_square: list[list[int]], verbose: bool | None = False):
    """
    Backtracking algorithm where valid solutions are updated to
    the `LAST_KNOWN_GOOD_SOLUTION` variable. There might be multiple
    correct answers to the sudoku, hence "last_known_..."
    """

    # Cycle through all cells in sudoku square
    for x, y in ALL_XYS:
        # If cell is empty then attempt fill in
        if not sudoku_square[x][y]:
            for i in range(1, 10):

                # If valid option found fill in the cell and
                # try arriving at a solution with the use of recursion
                if check_insert(sudoku_square, x, y, i):
                    sudoku_square[x][y] = i
                    solve(sudoku_square, verbose)
                    sudoku_square[x][y] = 0
            return

    if verbose:
        print("Found Solution:")
        pprint(sudoku_square)
        input("Continue?")

    global LAST_KNOWN_GOOD_SOLUTION
    LAST_KNOWN_GOOD_SOLUTION = copy.deepcopy(sudoku_square)


def solve_and_return_result(sudoku_square: list[list[int]]) -> list[list[int]]:
    """
    Solve and return the completed sudoku.
    Note: final return statement in solve() did not work. Any idea why?
    """
    solve(sudoku_square)
    return LAST_KNOWN_GOOD_SOLUTION


if __name__ == "__main__":

    # Select a sudoku problem
    # sudoku = starter_sudoku_sets.MEDIUM_SUDOKU
    sudoku = example_problems.DIFFICULT_SUDOKU

    # Get a possible complete solution
    # completed_sudoku = solve_and_return_result(sudoku)
    # print("Completed sudoku")
    # pprint(completed_sudoku)

    # Get all possible solutions to a sudoku printed in terminal
    solve(sudoku, verbose=True)
    print("Completed sudoku")
    pprint(LAST_KNOWN_GOOD_SOLUTION)