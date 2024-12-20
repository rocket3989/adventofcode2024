from aocd import get_data
from parse import parse, findall, search
from rich import print as print
from collections import defaultdict, deque, Counter
import functools
from heapq import heappop, heappush
from itertools import permutations, product
import re
from tqdm import tqdm
import resource
import sys
from z3 import Int, Optimize, sat, Solver

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

data = get_data(day=18, year=2024)


test_data ='''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''


def solve1(data: str) -> int:
    # first_line = search("{}\n", data)[0]
    # ns = [int(x) for x in data.split('\n')]
    parsed = [(tuple(r)) for r in findall("{:d},{:d}", data)]

    # matrix_data = data.split("\n")
    # n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    
    
    n, m = 71, 71
    for i in range(n):
        for j in range(m):
            matrix[i][j] = '.'

    i = 0
    for x, y in parsed:
        matrix[x][y] = '#'
        i += 1
        if i == 1024:
            break

    ans = 0

    seen = set()

    q = deque([(0, 0, 0)])
    while q:
        x, y, dist = q.popleft()
        # print(x, y, dist)

        if matrix[x][y] != '.':
            continue

        if (x, y) in seen:
            continue
        seen.add((x, y))

        if x == n - 1 and y == m - 1:
            ans = dist
            break
        
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            q.append((x + dx, y + dy, dist + 1))


    return ans


def solve2(data: str) -> int:
        # first_line = search("{}\n", data)[0]
    # ns = [int(x) for x in data.split('\n')]
    parsed = [(tuple(r)) for r in findall("{:d},{:d}", data)]

    print(len(parsed))

    # matrix_data = data.split("\n")
    # n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    
    
    n, m = 71, 71
    for i in range(n):
        for j in range(m):
            matrix[i][j] = '.'

    i = 0
    for x, y in parsed[:1024]:
        matrix[x][y] = '#'
        i += 1
    
    c = 1023

    for i, j in parsed[1024:]:

        matrix[i][j] = '#'
        c += 1
        

        seen = set()

        q = deque([(0, 0, 0)])
        while q:
            x, y, dist = q.popleft()

            if matrix[x][y] != '.':
                continue

            if (x, y) in seen:
                continue
            seen.add((x, y))

            if x == n - 1 and y == m - 1:
                break
            
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                q.append((x + dx, y + dy, dist + 1))
        else:
            return (i, j)


# print(solve1(test_data))
print(solve1(data))
# print(solve2(test_data))
print(solve2(data))