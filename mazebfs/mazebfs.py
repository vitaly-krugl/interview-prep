# coding=utf-8
"""
Finds shortest path in maze using BFS (Breadth First Search).

Assumes maze with walls marked as # (hash) characters. Navigable
space is represented by space characters. @ (at sign) marks start
and $ (US Dollar) marks end.

Can move only vertically and horizontally, not diagonally.

Example maze:

maze = [
"####$##",
"#     #",
"# ### #",
"# #@  #",
"# ##  #",
"#     #",
"#######"
]

might result in the following path via BFS:

####$##
#   ↑←#
# ###↑#
# #→→↑#
# ##  #
#     #
#######

"""


from copy import deepcopy


GOAL_SYM = "$"
START_SYM = "@"
WALL_SYM = "#"
PASSAGE_SYM = " "
PATH_SYM_MAP = { # mapping of (row, col) offsets to navigation symbols
    (0, -1): "←", # left
    (0, 1):  "→", # right
    (-1, 0): "↑", # up
    (1, 0):  "↓"  # down
}


def _candidateNeighbors(maze, cellR, cellC):
    return [(r, c) for r, c in (
                (cellR, cellC-1),
                (cellR, cellC+1),
                (cellR-1, cellC),
                (cellR+1, cellC))
            if (r >= 0 and r < len(maze) and c >= 0 and c < len(maze[r]) and
                maze[r][c] != WALL_SYM)
    ]

def findShortestPath(maze):
    """

    :param maze: Represents maze and start/goal locations. See file docstring
      description. No validation is performed on input in this exploratory
      solution. The input data is not modified by this function.
    :return: a sequence of 0-based row/column coordinates representing a
      shortest path from start to goal, inclusively.
    """
    # Convert the maze into a two-dimensional array
    maze = [ list(line) for line in maze]

    # First, locate the goal's coordinates
    goalR = goalC = -1
    for goalR in xrange(len(maze)):
        try:
            goalC = maze[goalR].index(GOAL_SYM)
        except ValueError:
            continue
        else:
            break
    else:
        raise ValueError("Goal ({}) not found".format(GOAL))

    assert goalR >= 0 and goalC >= 0

    # DFS until start is reached
    workQueue = [(goalR, goalC)]
    maze[goalR][goalC] = 0 # distance from goal to goal itself is 0
    startR = startC = -1
    while workQueue and startC == -1:
        # Dequeue the oldest cell coordinate
        cellR, cellC = workQueue.pop(0)
        neighborDepth = maze[cellR][cellC] + 1

        for nR, nC in _candidateNeighbors(maze, cellR, cellC):
            if maze[nR][nC] == START_SYM:
                startR, startC = nR, nC
                maze[nR][nC] = neighborDepth
                break

            elif maze[nR][nC] == PASSAGE_SYM:
                maze[nR][nC] = neighborDepth
                workQueue.append((nR, nC))

    if startR == -1:
         raise ValueError("Start ({}) not found".format(START_SYM))

    # Construct path from start to goal
    path = [(startR, startC)]
    cellR, cellC = startR, startC

    while maze[cellR][cellC] != 0:
        # Find neighbor with decreasing distance
        for nR, nC in _candidateNeighbors(maze, cellR, cellC):
            if maze[nR][nC] != PASSAGE_SYM and maze[nR][nC] < maze[cellR][cellC]:
                cellR, cellC = nR, nC
                path.append((cellR, cellC))
                break
        else:
            raise Exception("Logic error: failed to find next path node from "
                            "{},{}".format(cellR, cellC))

    return path


def plotShortestPath(maze):
    """Find and plot shortest path in the maze.

    :param maze: see findShortestPath
    :return: None
    """
    path = findShortestPath(maze)

    # Transform maze into a two-dimensional array of rows and columns
    maze = [list(row) for row in maze]

    # Mark path in maze
    for i, (r, c) in enumerate(path):
        if i == len(path) - 1:
            maze[r][c] = GOAL_SYM
        else:
            nextR, nextC = path[i+1]
            maze[r][c] = PATH_SYM_MAP[(nextR-r, nextC-c)]

    # Print maze with path
    for row in maze:
        print "".join(row)
