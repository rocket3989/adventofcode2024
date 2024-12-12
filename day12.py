from aocd import get_data
from rich import print as print
from collections import defaultdict, deque

data = get_data(day=12, year=2024)


test_data ='''AAB
ABA
BAA'''

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
            if matrix[i][j] == '':
                continue

            q = deque()
            curr = matrix[i][j]
            area = 0
            perimeter = 0
            seen = set()
            
            q.append((i, j))

            while q:
                x, y = q.popleft()

                if (x, y) in seen:
                    continue
                
                if matrix[x][y] != curr:
                    perimeter += 1
                    continue

                matrix[x][y] = ''
                seen.add((x, y))
                area += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    q.append((x + dx, y + dy))

            ans += area * perimeter

    return ans


def solve2(data: str) -> int:

    matrix_data = data.split("\n")
    n, m = len(matrix_data), len(matrix_data[0])
    matrix = defaultdict(lambda: defaultdict(str))
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix_data[i][j]

    ans = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '':
                continue

            q = deque()
            curr = matrix[i][j]
            area = 0
            edges = 0
            seen = set()
            
            q.append((i, j))

            while q:
                x, y = q.popleft()

                if (x, y) in seen:
                    continue
                
                seen.add((x, y))
                area += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                    if matrix[x + dx][y + dy] == curr:
                        q.append((x + dx, y + dy))
                        continue
                    
                    for offset in [-1, 1]:

                        if dy == 0:
                            if matrix[x][y + offset] != curr:
                                edges += 1
                            elif matrix[x + dx][y + offset] == curr:
                                edges += 1

                        if dx == 0:
                            if matrix[x + offset][y] != curr:
                                edges += 1
                            elif matrix[x + offset][y + dy] == curr:
                                edges += 1

            for x, y in seen:
                matrix[x][y] = ''

            ans += area * (edges // 2)
                

    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))