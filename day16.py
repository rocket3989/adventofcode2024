from aocd import get_data
from rich import print as print
from heapq import heappop, heappush
from collections import defaultdict

data = get_data(day=16, year=2024)


test_data ='''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''


def solve1(data: str) -> int:

    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):
            if matrix_data[i][j] == 'S':
                start = (i, j)
                matrix[i][j] = '.'
            elif matrix_data[i][j] == 'E':
                end = (i, j)
                matrix[i][j] = '.'
            else:
                matrix[i][j] = matrix_data[i][j]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    h = [(0, start[0], start[1], 1)]

    seen = set()

    while h:
        dist, x, y, dir = heappop(h)

        if (x, y, dir) in seen:
            continue

        seen.add((x, y, dir))
        if (x, y) == end:
            return dist

        for new_dir, (dx, dy) in enumerate(dirs):

            if matrix[x + dx][y + dy] != '#':
                heappush(h, (dist + 1 + 1000 * (new_dir != dir), x + dx, y + dy, new_dir))



def solve2(data: str) -> int:
    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):
            if matrix_data[i][j] == 'S':
                start = (i, j)
                matrix[i][j] = '.'
            elif matrix_data[i][j] == 'E':
                end = (i, j)
                matrix[i][j] = '.'
            else:
                matrix[i][j] = matrix_data[i][j]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    h = [(0, start[0], start[1], 1, [])]

    seen = defaultdict(lambda: 10000000000)

    best_paths = defaultdict(set)

    while h:
        dist, x, y, dir, path = heappop(h)

        if seen[(x, y, dir)] < dist:
            continue

        seen[(x, y, dir)] = dist
        if (x, y) == end:
            if best_paths and not best_paths[dist]:
                break

            best_paths[dist] |= set(path)
            continue

        for new_dir, (dx, dy) in enumerate(dirs):

            if matrix[x + dx][y + dy] != '#':
                heappush(h, (dist + 1 + 1000 * (new_dir != dir), x + dx, y + dy, new_dir, path + [(x, y)]))

    return len(list(best_paths.values())[0]) + 1

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))