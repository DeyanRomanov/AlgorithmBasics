"""
    You are given a labyrinth. Your goal is to find all paths from the start (cell 0, 0) to the exit, marked with 'e'.
    · Empty cells are marked with a dash '-'.
    · Walls are marked with a star '*'.
    On the first line, you will receive the dimensions of the labyrinth. Next, you will receive the actual labyrinth.
    The order of the paths does not matter.
"""

labyrinth_row = int(input())
labyrinth_col = int(input())

labyrinth = []
walls = []
start_position = ''


def create_labyrinth(matrix, lab_row, lab_col):
    wall = []
    start = ''
    for r in range(lab_row):
        matrix.append(input().split())
        for c in range(lab_col):
            if matrix[r][c] == 'e':
                start = r, c
            elif matrix[r][c] == '*':
                wall.append((r, c))

    return matrix, wall, start


labyrinth, walls, start_position = create_labyrinth(labyrinth, labyrinth_row, labyrinth_col)


def recursive_find_path(lab, wall, position, path, row, col):

    pass

print(walls)
print(start_position)
