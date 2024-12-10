from aocd import get_data
from rich import print as print
from collections import defaultdict
import functools


data = get_data(day=10, year=2024)


test_data ='''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''


def solve1(data: str) -> int:

    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    starts = []
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(matrix_data[i][j])
            if matrix[i][j] == 0:
                starts.append((i, j))

    @functools.cache
    def dfs(x, y):
        if matrix[x][y] == 9:
            return frozenset([(x, y)])
        
        ret = set()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if matrix[x + dx][y + dy] == matrix[x][y] + 1:
                ret |= set(dfs(x + dx, y + dy))
        return frozenset(ret)

    ans = 0

    for x, y in starts:
        ans += len(dfs(x, y))

    return ans


def solve2(data: str) -> int:

    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    starts = []
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(matrix_data[i][j])
            if matrix[i][j] == 0:
                starts.append((i, j))

    @functools.cache
    def dfs(x, y):
        if matrix[x][y] == 9:
            return 1
        
        ret = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if matrix[x + dx][y + dy] == matrix[x][y] + 1:
                ret += dfs(x + dx, y + dy)
        return ret

    ans = 0

    for x, y in starts:
        ans += dfs(x, y)

    return ans


print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))