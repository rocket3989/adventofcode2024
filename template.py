from aocd import get_data
from parse import parse, findall, search
from rich import print as print
from collections import defaultdict, deque, Counter
from functools import cache
from heapq import heappop, heappush
from itertools import permutations, product
import re
from tqdm import tqdm
import resource
import sys
from z3 import Int, Optimize, sat, Solver

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

data = get_data(day=13, year=2024)


test_data =''''''


def solve1(data: str) -> int:
    # first_line = search("{}\n", data)[0]
    # ns = [int(x) for x in data.split('\n')]
    # parsed = [(tuple(r)) for r in findall("mul({:d},{:d})", data)]

    # matrix_data = data.split("\n")
    # n, m = len(matrix_data), len(matrix_data[0])
    # matrix = defaultdict(lambda: defaultdict(str))
    # for i in range(n):
    #     for j in range(m):
    #         matrix[i][j] = matrix_data[i][j]

    ans = 0

    return ans


def solve2(data: str) -> int:
    ans = 0


    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))