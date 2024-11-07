import heapq
from collections import deque
from copy import deepcopy
from typing import List, Tuple, Callable

from consts import TARGET_MATRIX, EMPTY_CELL
from models.direction import Direction
from models.matrix import Matrix
from models.orbit import Orbit
from utils.user_input import generate_example_matrix, generate_user_args_matrix


def bfs(matrix: Matrix, target_matrix: Matrix) -> Tuple[Orbit, int]:
    """
    BFS algorithm - Breath first search
    Standard uninformed bfs search
    I used queue in order to implement bfs


    :return: the orbit of the solution, and total steps
    """

    visited = set()
    current_orbit: Orbit = []

    queue = deque()
    queue.append((matrix, tuple(current_orbit)))

    while matrix != target_matrix:

        matrix, current_orbit = queue.popleft()
        visited.add(matrix)

        for direction in Direction:
            if not matrix.is_move_valid(EMPTY_CELL, direction):
                continue
            next_matrix = matrix.move_element(EMPTY_CELL, direction)
            if next_matrix not in visited:
                queue.append((next_matrix, current_orbit[:] + tuple([direction])))

    return current_orbit, len(visited)


def iddfs(matrix: Matrix, target_matrix: Matrix) -> Tuple[Orbit, int]:
    """
    IDDFS algorithm - uninformed iterative deepening depth search
        1. Run dfs search with limit of depth x
        2. After iteration that not found the target depth x = x + 1
        3. Back to 1
    I used recursion method with use of global variables

    :return: the orbit of the solution, and total steps
    """

    visited = {matrix}
    solution_orbit: Orbit | None = None

    def dfs_rec(current_matrix: Matrix, current_orbit: Orbit, current_depth: int, max_depth: int):
        nonlocal solution_orbit, visited

        if current_matrix == target_matrix:
            solution_orbit = current_orbit
            return

        if current_depth == max_depth:
            return

        visited.add(current_matrix)

        for direction in Direction:
            if not current_matrix.is_move_valid(EMPTY_CELL, direction):
                continue

            next_matrix = current_matrix.move_element(EMPTY_CELL, direction)
            if next_matrix not in visited:
                copy_orbit = deepcopy(current_orbit)
                copy_orbit.append(direction)
                dfs_rec(next_matrix, copy_orbit, current_depth + 1, max_depth)

    depth = 1
    while solution_orbit is None:
        visited = {matrix}
        dfs_rec(matrix, [], 0, depth)
        depth += 1

    return solution_orbit, len(visited)


def gbfs(matrix: Matrix, target_matrix: Matrix) -> Tuple[Orbit, int]:
    """
    GBFS algorithm - Greedy best first search.
    Search by heuristic function, select the next minimum cost state, min(h(n))

    :return: the orbit of the solution, and total steps
    """

    visited = set()
    current_orbit: Orbit = []

    heap = []
    heapq.heappush(heap, (matrix.mse_heuristic(target_matrix), matrix, tuple(current_orbit)))

    while matrix != target_matrix:

        _, matrix, current_orbit = heapq.heappop(heap)
        visited.add(matrix)

        for direction in Direction:
            if not matrix.is_move_valid(EMPTY_CELL, direction):
                continue

            next_matrix = matrix.move_element(EMPTY_CELL, direction)
            if next_matrix not in visited:
                heapq.heappush(heap,
                               (next_matrix.mse_heuristic(target_matrix),
                                next_matrix,
                                current_orbit[:] + tuple([direction])))

    return current_orbit, len(visited)


def a_star(matrix: Matrix, target_matrix: Matrix) -> Tuple[Orbit, int]:
    """
    A* algorithm - a star algorithm.
    Search by heuristic function, select the next total minimum cost state, min(g(n) + h(n))

    :return: the orbit of the solution, and total steps
    """

    visited = set()
    current_orbit: Orbit = []

    heap = []
    heapq.heappush(heap, (matrix.mse_heuristic(target_matrix), matrix, tuple(current_orbit)))

    while matrix != target_matrix:

        current_cost, matrix, current_orbit = heapq.heappop(heap)
        visited.add(matrix)

        for direction in Direction:
            if not matrix.is_move_valid(EMPTY_CELL, direction):
                continue

            next_matrix = matrix.move_element(EMPTY_CELL, direction)
            if next_matrix not in visited:
                heapq.heappush(heap,
                               (next_matrix.mse_heuristic(target_matrix) + current_cost,
                                next_matrix,
                                current_orbit[:] + tuple([direction])))

    return current_orbit, len(visited)


def main():
    # Target matrix

    print(f'Target matrix: \n{TARGET_MATRIX}')

    # Input matrix
    # input_matrix = generate_user_args_matrix()
    input_matrix = generate_example_matrix()
    print(f'Input matrix: \n{input_matrix}')

    # Algorithms run
    algorithms: List[Callable[[Matrix, Matrix], Tuple[Orbit, int]]] = [
        bfs,
        iddfs,
        gbfs,
        a_star
    ]
    for algorithm in algorithms:
        print(f'\nAlgorithm {algorithm.__name__} -')

        steps: int
        orbit: Orbit
        orbit, steps = algorithm(input_matrix, TARGET_MATRIX)

        print(f'Total steps: {steps}')
        print(f'Solution orbit: {orbit}')
        print(f'Solution orbit length: {len(orbit)}')


if __name__ == '__main__':
    main()
