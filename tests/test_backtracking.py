import pytest

from src.helpers.errors import SolverTimeoutError, UnknownSolutionError
from src.solutions.backtracking_solution import solve_square
from src.sudoku_cube import Sudoku
from tests.data import EASY_SUDOKU, SOLVED_SUDOKU, UNSOLVABLE_SUDOKU

SUDOKU = Sudoku(EASY_SUDOKU)
SUDOKU.run_solver(solve_square)

test_solution_and_length_of_suggestions = [
    (SUDOKU.solutions[0], SOLVED_SUDOKU),
    (len(SUDOKU.solutions), 1),
    (len(SUDOKU.suggestions.keys()), 3),
]

test_suggestions = [
    ((2, 2), [4]),
    ((5, 6), [2]),
    ((6, 1), [9]),
]


@pytest.mark.parametrize("test_data,expected", test_solution_and_length_of_suggestions)
def test_easy_backtracking_solution(test_data, expected):
    assert test_data == expected


@pytest.mark.parametrize("test_data,expected", test_suggestions)
def test_easy_backtracking_suggestions(test_data, expected):
    assert SUDOKU.suggestions[test_data] == expected


def test_unsolvable_problem():
    sudoku = Sudoku(UNSOLVABLE_SUDOKU)
    with pytest.raises(UnknownSolutionError):
        sudoku.run_solver(solve_square)


def test_timeout():
    sudoku = Sudoku(EASY_SUDOKU)
    with pytest.raises(SolverTimeoutError):
        sudoku.run_solver(solve_square, start_time=0, timeout=0.001)
