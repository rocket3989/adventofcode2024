from aocd import get_data
from rich import print
from collections import defaultdict, Counter

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
    matrix = data.split("\n")
    n, m = len(matrix), len(matrix[0])
    matrix = [[matrix[i][j] for j in range(m)] for i in range(n)]
    ans = 0


    for i in range(n):
        for j in range(m):
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

                for pos, char in enumerate("XMAS"):
                    if (i + dir[0] * pos < 0 or 
                        j + dir[1] * pos < 0 or 
                        i + dir[0] * pos >= n or 
                        j + dir[1] * pos >= m or
                        matrix[i + dir[0] * pos][j + dir[1] * pos] != char):
                        break
                else:
                    ans += 1


    return ans

def solve2(data: str) -> int:
    matrix = data.split("\n")
    n, m = len(matrix), len(matrix[0])
    matrix = [[matrix[i][j] for j in range(m)] for i in range(n)]

    a_loc = defaultdict(int)

    for i in range(n):
        for j in range(m):
            for dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                for pos, char in enumerate("MAS"):
                    if (i + dir[0] * pos < 0 or 
                        j + dir[1] * pos < 0 or 
                        i + dir[0] * pos >= n or 
                        j + dir[1] * pos >= m or
                        matrix[i + dir[0] * pos][j + dir[1] * pos] != char):
                        break
                else:
                    a_loc[(i + dir[0], j + dir[1])] += 1
    
    return Counter(a_loc.values())[2]
                
                
print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))