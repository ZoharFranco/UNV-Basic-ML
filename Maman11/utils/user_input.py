import argparse

from models.matrix import Matrix


def generate_user_args_matrix() -> Matrix:
    parser = argparse.ArgumentParser(description="Process a list of numbers.")
    parser.add_argument("numbers", type=int, nargs="+", help="A list of integers")
    args = parser.parse_args()
    args.numbers.append(-1)
    input_matrix: Matrix = Matrix.from_list_and_size(args.numbers, int(len(args.numbers) ** 0.5))
    return input_matrix


def generate_example_matrix() -> Matrix:
    lst = [[3, 1, 2], [6, 4, -1], [7, 8, 5]]
    input_matrix: Matrix = Matrix(lst)
    return input_matrix
