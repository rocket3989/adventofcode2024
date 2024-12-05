from aocd import get_data
from parse import findall
from rich import print
from collections import defaultdict
import functools

data = get_data(day=5, year=2024)


test_data ='''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''


def solve1(data: str) -> int:
    ans = 0
    data2 = data.split("\n\n")[1]

    rules = [(tuple(r)) for r in findall("{:d}|{:d}", data)]
    wrong = defaultdict(set)

    for a, b in rules:
        wrong[b].add(a)

    for line in data2.split("\n"):
        line = [int(x) for x in line.split(",")]
        
        bad = False
        for i, val in enumerate(line):
            for val2 in line[i + 1:]:
                if val2 in wrong[val]:
                    bad = True
                    break
            else:
                continue
            break
        
        if not bad:
            ans += line[len(line) // 2]

    return ans

def solve2(data: str) -> int:

    ans = 0
    data2 = data.split("\n\n")[1]
    rules = [(tuple(r)) for r in findall("{:d}|{:d}", data)]

    wrong = defaultdict(set)

    for a, b in rules:
        wrong[b].add(a)

    for line in data2.split("\n"):
        line = [int(x) for x in line.split(",")]
        
        bad = False
        for i, val in enumerate(line):
            for val2 in line[i + 1:]:
                if val2 in wrong[val]:
                    bad = True
                    break
            else:
                continue
            break
        
        if not bad:
            continue

        
        line.sort(key=functools.cmp_to_key(lambda x, y: -1 if y in wrong[x] else 1))
        ans += line[len(line) // 2]

        
    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))