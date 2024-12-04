from aocd import get_data
from parse import findall
from rich import print
from collections import Counter

data = get_data(day=1, year=2024)

test_data ='''3   4
4   3
2   5
1   3
3   9
3   3'''


def solve1(data: str) -> int:
    parsed = [(tuple(r)) for r in findall("{:d}   {:d}", data)]

    left = [x[0] for x in parsed]
    right = [x[1] for x in parsed]

    left.sort()
    right.sort()

    ans = 0
    for l, r in zip(left, right):
        ans += abs(l - r)

    return ans

def solve2(data: str) -> int:
    parsed = [(tuple(r)) for r in findall("{:d}   {:d}", data)]

    left = [x[0] for x in parsed]
    right = Counter([x[1] for x in parsed])

    ans = 0
    for l in left:
        ans += l * right[l]

    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))
