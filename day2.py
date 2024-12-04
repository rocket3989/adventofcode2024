from aocd import get_data
from parse import findall
from rich import print


data = get_data(day=2, year=2024)

test_data ='''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

def solve1(data: str) -> int:
    parsed = [[r[0] for r in findall("{:d}", line)] for line in data.split('\n')]

    ans = 0
    for line in parsed:
        if line[0] == line[1]:
            continue

        if line[0] > line[1]:
            for a, b in zip(line, line[1:]):
                if a <= b or a - b > 3:
                    break
            else:
                ans += 1
        else:
            for a, b in zip(line, line[1:]):
                if a >= b or b - a > 3:
                    break
            else:
                ans += 1

    return ans

def solve2(data: str) -> int:
    parsed = [[r[0] for r in findall("{:d}", line)] for line in data.split('\n')]

    ans = 0
    for line in parsed:

        for pos in range(0, len(line)):
            curr = line[:pos] + line[pos + 1:]

            if curr[0] == curr[1]:
                continue

            if curr[0] > curr[1]:
                for a, b in zip(curr, curr[1:]):
                    if a <= b or a - b > 3:
                        break
                else:
                    ans += 1
                    break
            else:
                for a, b in zip(curr, curr[1:]):
                    if a >= b or b - a > 3:
                        break
                else:
                    ans += 1
                    break

    return ans


print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))