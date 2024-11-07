from copy import deepcopy
from typing import List, Tuple

from models.direction import Direction


class Matrix:

    # Constructors
    def __init__(self, matrix: List[List[int]] = None):
        self.matrix = matrix

    @classmethod
    def from_list_and_size(cls, lst: List[int], size: int):
        return cls([lst[i:i + size] for i in range(0, len(lst), size)])

    # Attributes
    def size(self) -> int:
        return len(self.matrix)

    # Functions

    def index(self, value: int) -> Tuple[int, int]:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == value:
                    return i, j

    def is_swap_valid(self, i1: int, j1: int, i2: int, j2: int) -> bool:
        return 0 <= i1 < self.size() and 0 <= j1 < self.size() and 0 <= i2 < self.size() and 0 <= j2 < self.size()

    def swap(self, i1: int, j1: int, i2: int, j2: int):
        if self.is_swap_valid(i1, j1, i2, j2):
            self.matrix[i1][j1], self.matrix[i2][j2] = self.matrix[i2][j2], self.matrix[i1][j1]

    def is_move_valid(self, value: int, direction: Direction) -> bool:
        i1, j1 = self.index(value)
        i2, j2 = i1 + direction.value[0], j1 + direction.value[1]
        return self.is_swap_valid(i1, j1, i2, j2)

    def move_element(self, value: int, direction: Direction) -> 'Matrix':
        i1, j1 = self.index(value)
        i2, j2 = i1 + direction.value[0], j1 + direction.value[1]
        new_matrix = deepcopy(self)
        new_matrix.swap(i1, j1, i2, j2)
        return new_matrix

    def mse_heuristic(self, other) -> float:
        if not isinstance(other, Matrix):
            return 0

        mse = 0
        for i in range(self.size()):
            for j in range(self.size()):
                value = self.matrix[i][j]
                i2, j2 = other.index(value)
                mse += ((i - i2) ** 2 + (j - j2) ** 2)

        return mse

    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix):
            return False
        return self.matrix == other.matrix

    def __repr__(self) -> str:
        return '\n'.join(str(row) for row in self.matrix)

    def __str__(self) -> str:
        return '\n'.join(str(row) for row in self.matrix)

    def __hash__(self) -> int:
        return tuple(map(tuple, self.matrix)).__hash__()

    def __ge__(self, other):
        return self

    def __gt__(self, other):
        return self
