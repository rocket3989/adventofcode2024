from aocd import get_data
from parse import parse, findall, search
from rich import print
from collections import defaultdict, deque, Counter
import functools
from heapq import heappop, heappush
from itertools import product
import re

data = get_data(day=4, year=2024)


test_data ='''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''


def solve1(data: str) -> int:
    # first_line = search("{}\n", data)[0]
    # ns = [int(x) for x in data.split('\n')]
    # parsed = [(tuple(r)) for r in findall("mul({:d},{:d})", data)]

    matrix = data.split("\n")
    n, m = len(matrix), len(matrix[0])
    matrix = [[matrix[i][j] for j in range(m)] for i in range(n)]
    ans = 0


    for i in range(n):
        for j in range(m):
            if matrix[i][j] != "X":
                continue

            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                try:
                    for pos, char in enumerate("MAS", 1):
                        if i + dir[0] * pos < 0 or j + dir[1] * pos < 0 or matrix[i + dir[0] * pos][j + dir[1] * pos] != char:
                            break
                    else:
                        ans += 1

                except:
                    continue



    return ans

def solve2(data: str) -> int:
    ans = 0

    matrix = data.split("\n")
    n, m = len(matrix), len(matrix[0])
    matrix = [[matrix[i][j] for j in range(m)] for i in range(n)]
    ans = 0


    aLoc = defaultdict(int)


    for i in range(n):
        for j in range(m):
            if matrix[i][j] != "M":
                continue

            for dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                try:
                    for pos, char in enumerate("AS", 1):
                        if i + dir[0] * pos < 0 or j + dir[1] * pos < 0 or matrix[i + dir[0] * pos][j + dir[1] * pos] != char:
                            break
                    else:
                        aLoc[(i + dir[0], j + dir[1])] += 1

                except:
                    continue
    
    # print(aLoc)
    ans = Counter(aLoc.values())[2] + Counter(aLoc.values())[3]
    return ans
                
print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))