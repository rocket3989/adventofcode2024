from aocd import get_data
from rich import print as print
from collections import defaultdict
# from z3 import Int, Optimize, sat, Solver

data = get_data(day=22, year=2024)


test_data ='''123'''


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

    for line in data.split('\n'):
        n = int(line)

        for _ in range(2000):
            n = ((n * 64) ^ n) % 16777216
            
            n = ((n // 32) ^ n) % 16777216
            n = ((n * 2048) ^ n) % 16777216

        print()
        ans += n
    return ans


def solve2(data: str) -> int:
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

    seq = defaultdict(int)

    for line in data.split('\n'):
        n = int(line)
        seen = set()

        last4 = []
        prev = None

        for _ in range(2001):
            if prev is not None:
                last4.append((n % 10) - prev)
                if len(last4) > 4:
                    last4.pop(0)
                
                if len(last4) == 4 and tuple(last4) not in seen:
                    seq[tuple(last4)] += n % 10
                    seen.add(tuple(last4))
            prev = n % 10
            n = ((n * 64) ^ n) % 16777216
            n = ((n // 32) ^ n) % 16777216
            n = ((n * 2048) ^ n) % 16777216

    
    ans = max(seq.values())
    return ans  


    # print(solve1(test_data))
    # print(solve1(data))
print(solve2(test_data))
print(solve2(data))