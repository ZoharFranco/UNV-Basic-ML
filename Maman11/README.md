# General Overview

## Algorithms and Functions:

tiles.py contains all the algorithms logic

- BFS - def bfs(matrix: Matrix, target_matrix: Matrix) -> Tuple[Orbit, int]:
- IDDFS - def iddfs(matrix: Matrix, target_matrix: Matrix) -> Tuple[Orbit, int]:
- GBFS - def a_star(matrix: Matrix, target_matrix: Matrix) -> Tuple[Orbit, int]:
- A* - def a_star(matrix: Matrix, target_matrix: Matrix) -> Tuple[Orbit, int]:
- Main create input matrix and run each algorithm on it.

utils/user_input.py contains user input parsing and input.

models - contains useful objects.

- matrix.py - object that contain matrix as list of lists and functionality on it.
- direction.py - enum of all the horizontal vertical directions.
- orbit.py - type of list of direction as orbit of one cell.

## Data structures:

- BFS - queue (get last inserted node not by some value)
- IDFFS - no unique data structure (recursion)
- GBFS - heap (queue to get minimum heuristic value by O(n))
- A* - heap (queue to get minimum heuristic value by O(n))

# Space overview

## States

Unique matrix is a state in the space, 10! because every cell can be in different location in the matrix 10 * 9 * 8 * ..

## Action / Transition

Can be tile that we replace with the empty cell \ direction that we move the empty tile in.
In my implementation I chose direction as the action.
(This is the only move that can matrix transit by)

# Heuristic function

I chose something close to MSE but without square and by axis as heuristic function,
this is a common and easy heuristic function.
my MSE = (x1-x2)^2 + (y1 - y2)^2

## Admissibility

For every not same cell:
(x1-x2)^2 + (y1-y2)^2 <=  (x1-x2) + (y1-y2) == Total steps \ Actual value => admissible

## Consistency

Example of not consistent -
h(u1) of matrix with Cell that in 2 distance from target > h(u2) of matrix with cell that in 1 distance from target * 2
h(u1) = (2)^2 + (0)^2 = 4 >= 2 = ((1)^2 + (0)^2) + ((1)^2 + (0)^2) = h(u2) => not consistent

# Optimal orbit ?

- BFS - yes
- IDDFS - yes
- GBFS - yes
- A* - yes

    
