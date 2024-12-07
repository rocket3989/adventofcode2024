from aocd import get_data
from parse import findall
from rich import print
from itertools import product
from tqdm import tqdm

data = get_data(day=7, year=2024)

test_data ='''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''


def solve1(data: str) -> int:
    parsed = [(tuple(r)) for r in findall("{:d}: {}\n", data)]

    ans = 0

    for target, digits in tqdm(parsed):
        digits = [int(x) for x in digits.split(" ")]

        for prod in product(['*', '+'], repeat=len(digits) - 1):

            curr = int(digits[0])

            for op, digit in zip(prod, digits[1:]):
                if op == '*':
                    curr *= int(digit)
                else:
                    curr += int(digit)

            if curr == int(target):
                ans += int(target)
                break

    return ans

def solve2(data: str) -> int:
    parsed = [(tuple(r)) for r in findall("{:d}: {}\n", data)]
    ans = 0

    for target, digits in tqdm(parsed):
        digits = [int(x) for x in digits.split(" ")]

        for prod in product(['*', '+', '||'], repeat=len(digits) - 1):

            curr = int(digits[0])

            for op, digit in zip(prod, digits[1:]):
                if op == '||':
                    curr = int(str(curr) + str(digit))
                elif op == '*':
                    curr *= int(digit)
                else:
                    curr += int(digit)

            if curr == int(target):
                ans += int(target)
                break

    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))