from aocd import get_data
from rich import print
from collections import defaultdict, Counter
import regex as re
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
    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix_data[i][j]
    ans = 0


    for i in range(n):
        for j in range(m):
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

                for pos, char in enumerate("XMAS"):
                    if matrix[i + dir[0] * pos][j + dir[1] * pos] != char:
                        break
                else:
                    ans += 1


    return ans

def solve2(data: str) -> int:
    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix_data[i][j]


    a_loc = defaultdict(int)

    for i in range(n):
        for j in range(m):
            for dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                for pos, char in enumerate("MAS"):
                    if matrix[i + dir[0] * pos][j + dir[1] * pos] != char:
                        break
                else:
                    a_loc[(i + dir[0], j + dir[1])] += 1
    
    return Counter(a_loc.values())[2]
                
def solve1regex(data: str) -> int:
    matrix = data.split("\n")
    _, m = len(matrix), len(matrix[0])

    regex = '(XMAS)|(SAMX)'
    print(m)


    for dist in [m - 1, m, m + 1]:

        regex += f'|(X.{{{dist}}}M.{{{dist}}}A.{{{dist}}}S)'
        regex += f'|(S.{{{dist}}}A.{{{dist}}}M.{{{dist}}}X)'
    
    # regex = '(?=(' + regex + '))'
    print(regex)
    for match in re.findall(regex, '|'.join(matrix), overlapped=True):
        print(match)
    return len(re.findall(regex, '|'.join(matrix), overlapped=True))



print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))