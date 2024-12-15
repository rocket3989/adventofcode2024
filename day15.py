from aocd import get_data
from rich import print as print
from collections import defaultdict

data = get_data(day=15, year=2024)

test_data ='''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''


def solve1(data: str) -> int:

    grid, moves = data.split("\n\n")

    x, y = 0, 0
    matrix_data = grid.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix_data[i][j]

            if matrix[i][j] == '@':
                y, x = i, j
                matrix[i][j] = '.'

    dirs = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }
    moves = moves.replace('\n', '')

    for move in moves:

        
        dy, dx = dirs[move]

        boxes = []

        dist = 1
        while matrix[y + dy * dist][x + dx * dist] == 'O':
            boxes.append((y + dy * dist, x + dx * dist))
            dist += 1

        if matrix[y + dy * dist][x + dx * dist] == '#':
            continue
        x += dx
        y += dy

        for bx, by in boxes:
            matrix[bx][by] = '.'

        for bx, by in boxes:
            matrix[bx + dy][by + dx] = 'O'
    
    ans = 0


    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'O':
                ans += i * 100 + j




    return ans


def solve2(data: str) -> int:

    grid, moves = data.split("\n\n")
    x, y = 0, 0
    matrix_data = grid.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):

            if matrix_data[i][j] == '.':
                matrix[i][j * 2] = '.'
                matrix[i][j * 2 + 1] = '.'

            if matrix_data[i][j] == '#':
                matrix[i][j * 2] = '#'
                matrix[i][j * 2 + 1] = '#'

            if matrix_data[i][j] == 'O':
                matrix[i][j * 2] = '['
                matrix[i][j * 2 + 1] = ']'
            
            if matrix_data[i][j] == '@':
                matrix[i][j * 2] = '.'
                matrix[i][j * 2 + 1] = '.'
                y, x = i, j * 2

    dirs = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }
    moves = moves.replace('\n', '')


    for move in moves:

        dy, dx = dirs[move]

        boxes = set()

        collision_front = set([(y + dy, x + dx)])

        while collision_front:
            new_collision_front = set()

            for cy, cx in collision_front:
                if matrix[cy][cx] == '#':
                    break
                
                if matrix[cy][cx] == '[':

                    if (cy, cx) in boxes:
                        continue

                    
                    boxes.add((cy, cx))
                    new_collision_front.add((cy + dy, cx + dx))
                    new_collision_front.add((cy + dy, cx + dx + 1))
                
                if matrix[cy][cx] == ']':

                    if (cy, cx - 1) in boxes:
                        continue
                    boxes.add((cy, cx - 1))
                    new_collision_front.add((cy + dy, cx + dx))
                    new_collision_front.add((cy + dy, cx + dx - 1))
            
            else:
                collision_front = new_collision_front
                continue
            break

        else:
            x += dx
            y += dy

            for by, bx in boxes:
                matrix[by][bx] = '.'
                matrix[by][bx + 1] = '.'

            for by, bx in boxes:
                matrix[by + dy][bx + dx] = '['
                matrix[by + dy][bx + dx + 1] = ']'

    
    ans = 0

    for i in range(n * 2):
        for j in range(m * 2):
            if matrix[i][j] == '[':
                ans += i * 100 + j


    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))