from aocd import get_data
from rich import print
from collections import defaultdict
from tqdm import tqdm

data = get_data(day=6, year=2024)

test_data ='''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''


def solve1(data: str) -> int:
    # first_line = search("{}\n", data)[0]
    # ns = [int(x) for x in data.split('\n')]
    # parsed = [(tuple(r)) for r in findall("mul({:d},{:d})", data)]

    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))

    seen = set()
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix_data[i][j]
            if matrix[i][j] == '^':
                x, y = i, j

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir = 0
    
    while matrix[x][y] != '':
        if matrix[x][y] == '#':
            x, y = x - dirs[curr_dir][0], y - dirs[curr_dir][1]
            curr_dir = (curr_dir + 1) % 4
            continue
            
        seen.add((x, y))
        x, y = x + dirs[curr_dir][0], y + dirs[curr_dir][1]


    return len(seen)

def solve2(data: str) -> int:
    ans = 0

    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))

    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix_data[i][j]
            if matrix[i][j] == '^':
                x_start, y_start = i, j

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir = 0
    
    for i in tqdm(range(n)):
        for j in range(m):
            if matrix[i][j] == '#':
                continue

            x, y = x_start, y_start
            seen = set()
            curr_dir = 0

            matrix[i][j] = '#'
            while matrix[x][y] != '':
                if matrix[x][y] == '#':
                    x, y = x - dirs[curr_dir][0], y - dirs[curr_dir][1]
                    curr_dir = (curr_dir + 1) % 4
                    continue

                if (x, y, curr_dir) in seen:
                    ans += 1
                    break
                    
                seen.add((x, y, curr_dir))
                x, y = x + dirs[curr_dir][0], y + dirs[curr_dir][1]

            matrix[i][j] = '.'
    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))