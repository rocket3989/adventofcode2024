from aocd import get_data
from rich import print
from collections import defaultdict

data = get_data(day=8, year=2024)


test_data ='''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''


def solve1(data: str) -> int:
    locs = defaultdict(list)
    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix_data[i][j]
            if matrix[i][j] != '.':
                locs[matrix[i][j]].append((i, j))

    pos = set()
    for loc_list in locs.values():
        for i, loc in enumerate(loc_list):
            for loc2 in loc_list[i + 1:]:

                vec = loc2[0] - loc[0], loc2[1] - loc[1]
                pos.add((loc[0] - vec[0], loc[1] - vec[1]))
                pos.add((loc2[0] + vec[0], loc2[1] + vec[1]))
    ans = 0

    for x, y in pos:
        if x >= 0 and x < n and y >= 0 and y < m:
            ans += 1

    return ans

def solve2(data: str) -> int:
    locs = defaultdict(list)
    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix_data[i][j]
            if matrix[i][j] != '.':
                locs[matrix[i][j]].append((i, j))

    pos = set()
    for loc_list in locs.values():
        for i, loc in enumerate(loc_list):
            for loc2 in loc_list[i + 1:]:
                vec = loc2[0] - loc[0], loc2[1] - loc[1]

                for i in range(50):
                    pos.add((loc[0] - i * vec[0], loc[1] - i * vec[1]))
                    pos.add((loc2[0] + i * vec[0], loc2[1] + i * vec[1]))

    ans = 0

    for x, y in pos:
        if x >= 0 and x < n and y >= 0 and y < m:
            ans += 1

    return ans


print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))