from aocd import get_data
from parse import parse, findall, search
from rich import print as print
from collections import defaultdict, deque, Counter
from functools import cache
from heapq import heapify, heappop, heappush
from itertools import permutations, product
import re
from tqdm import tqdm
import resource
import sys
from z3 import Int, Optimize, sat, Solver

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

data = get_data(day=20, year=2024)


test_data ='''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''


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
    
    distFromStart = defaultdict(int)
    distFromEnd = defaultdict(int)

    x, y = start

    q = deque([(x, y, 0)])
    while q:
        x, y, dist = q.popleft()
        if (x, y) in distFromStart:
            continue
        distFromStart[(x, y)] = dist

        if (x, y) == end:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] != '.':
                continue

            q.append((nx, ny, dist + 1))


    x, y = end

    q = deque([(x, y, 0)])
    while q:
        x, y, dist = q.popleft()
        if (x, y) in distFromEnd:
            continue
        distFromEnd[(x, y)] = dist

        if (x, y) == start:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] != '.':
                continue

            q.append((nx, ny, dist + 1))

    ans = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '#':
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if matrix[i + dx][j + dy] != '#':
                    continue
                if matrix[i + 2 * dx][j + 2 * dy] != '.':
                    continue


                dist = distFromStart[(i, j)] + distFromEnd[(i + 2 * dx, j + 2 * dy)] + 2
                if dist + 100 <= distFromStart[end]:
                    ans += 1
    return ans

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
    
    distFromStart = defaultdict(int)
    distFromEnd = defaultdict(int)

    x, y = start

    q = deque([(x, y, 0)])
    while q:
        x, y, dist = q.popleft()
        if (x, y) in distFromStart:
            continue
        distFromStart[(x, y)] = dist

        if (x, y) == end:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] != '.':
                continue

            q.append((nx, ny, dist + 1))


    x, y = end

    q = deque([(x, y, 0)])
    while q:
        x, y, dist = q.popleft()
        if (x, y) in distFromEnd:
            continue
        distFromEnd[(x, y)] = dist

        if (x, y) == start:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] != '.':
                continue

            q.append((nx, ny, dist + 1))

    ans = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '#':
                continue

            for dx in range(-20, 21):
                for dy in range(-20 + abs(dx), 21 - abs(dx)):
                    if matrix[i + dx][j + dy] != '.':
                        continue

                    dist = distFromStart[(i, j)] + distFromEnd[(i + dx, j + dy)] + dx + dy

                    if dist + 72 > distFromStart[end]:
                        continue

                    q = deque()

                    for dx2, dy2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if matrix[i + dx2][j + dy2] == '#':
                            q.append((i + dx2, j + dy2, 1))
                    seen = set()
                    
                    while q:
                        x, y, curr = q.popleft()
                        if (x, y) == (i + dx, j + dy):
                            dist = curr + distFromStart[(i, j)] + distFromEnd[(i + dx, j + dy)]
                            break
                        if (x, y) in seen:
                            continue
                        seen.add((x, y))

                        for dx2, dy2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            q.append((x + dx2, y + dy2, curr + 1))


                    for i2 in range(n):
                        for j2 in range(m):
                            if i2 == i + dx and j2 == j + dy:
                                print('X', end='')
                            elif i2 == i and j2 == j:
                                print('P', end='')
                            elif (i2, j2) == start:
                                print('S', end='')
                            elif (i2, j2) == end:
                                print('E', end='')
                            else:
                                print(matrix[i2][j2], end='')
                        print()
                    print(dist)
                    print()
                    print()
                    print()

                    if dist + 72 <= distFromStart[end]:
                        # for i2 in range(n):
                        #     for j2 in range(m):
                        #         if i2 == i + dx and j2 == j + dy:
                        #             print('X', end='')
                        #         elif i2 == i and j2 == j:
                        #             print('P', end='')
                        #         elif (i2, j2) == start:
                        #             print('S', end='')
                        #         elif (i2, j2) == end:
                        #             print('E', end='')
                        #         else:
                        #             print(matrix[i2][j2], end='')
                        #     print()
                        # print()
                        # print()
                        # print()
                        # print()
                        ans += 1
    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
# print(solve2(data))